from blog.models import Post, Blog, Image, Comment
from django.shortcuts import render_to_response, HttpResponseRedirect
from blog.forms import NewPostForm, NewImageForm, NewCommentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import forms as auth_form
from django.contrib.auth import logout, login, authenticate
import datetime

def login_view(request):
    if 'next' in request.GET:
        next = request.GET['next']
        next = next.split('/')
 #        next_blog_name = next[2]
#         if 'new_comment' in next:
#             next_type = next[4]
#             next_post_id = next[3]
#         else:
#             next_type = next[3]
# #
    else:
#       next = request.path
       next = request.POST['next']
       next = next.split('u')
       next_blog_name = next[3]
       next_blog_name = next_blog_name[1:-3]
       if 'new_comment' in next[5]:
           next_post_id = next[4]
           next_post_id = next_post_id[1:-3]
           next_type = next[5]
           next_type = next_type[1:-3]
       else:
           next_type = next[4]
           next_type = next_type[1:-3]
       
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # return HttpResponse('zalogowano do %s' % next_post_id)

                blog = Blog.objects.get(name = next_blog_name)
                blog_authors = Image.objects.values('author').distinct()
                if next_type == 'new_post':
                    form = NewPostForm({'blog': blog, 'comments': 0})    
                    return render_to_response('blog/new_image.html', {'form': form,
                                                                      'blog': blog,
                                                                      'blog_authors': blog_authors,
                                                                      },)
                elif next_type == 'new_image':
                    form = NewImageForm({'blog': blog, 'comments': 0})    
                    return render_to_response('blog/new_image.html', {'form': form,
                                                                      'blog': blog,
                                                                      'blog_authors': blog_authors,
                                                                      },)
                elif next_type == 'new_comment':
                    post = next_post_id
                    form = NewCommentForm({'post':post})
                    post = Post.objects.get(id = post)
                    all_comments = post.comment_set.all().order_by('-created')
                    return render_to_response('blog/new_comment.html', {'form': form,
                                                                        'post': post,
                                                                        'blog': blog,
                                                                        'comments': all_comments,})
                else:
                    return HttpResponse('cos poszlo nie tak, jak trzeba....')
        else:
            return HttpResponse('Podane konto nie istnieje!!')

    else:
        login_form = auth_form.AuthenticationForm()
        return render_to_response('blog/login_form.html', {'login_form':login_form,
                                                           'login_next': next,
                                                           })

def logout_view(request):
    logout(request)
    return HttpResponse("wylogowano")

    # return render_to_response('blog/list.html', {'blog': blog,
    #                                              'blogs': all_blogs,
    #                                              'blog_authors': blog_authors,
    #                                              'all_authors': all_authors,
    #                                              'posts': all_posts,
    #                                              'today': datetime.date.today().month,
    #                                              },
    #                           )

def blog(request, name = "empty"):
    if name == "empty":
        blog = Blog.objects.get(id = 1)
    else:
        blog = Blog.objects.get(name = name)

    all_blogs = Blog.objects.values('name').distinct()
    blog_authors = blog.post_set.values('author').distinct()
    all_authors = Post.objects.values('author').distinct()
    all_posts = blog.post_set.all().order_by('-created')

    return render_to_response('blog/list.html', {'blog': blog,
                                                 'blogs': all_blogs,
                                                 'blog_authors': blog_authors,
                                                 'all_authors': all_authors,
                                                 'posts': all_posts,
                                                 'today': datetime.date.today().month,
                                                 },
                              )

@login_required
def new_image(request, name):
    blog = Blog.objects.get(name = name)
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = blog
            post.save()
        else:
            return HttpResponse("Do dupy formularz!")
    else:
        blog_authors = Image.objects.values('author').distinct()
        form = NewImageForm({'blog': blog, 'comments': 0})    
        return render_to_response('blog/new_image.html', {'form': form,
                                                          'blog': blog,
                                                          'blog_authors': blog_authors,
                                                          },)
    return HttpResponseRedirect(reverse('blog.views.blog', args = (blog.name, )))
        
@login_required
def new_post(request, name):
    blog = Blog.objects.get(name = name)
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = blog
            post.save()
        else:
            return HttpResponse("Niepoprawnie wypelniony formularz.")

    else:
        blog_authors = Post.objects.values('author').distinct()
        form = NewPostForm({'blog': blog, 'comments': 0})    
        return render_to_response('blog/new_post.html', {'form': form,
                                                         'blog': blog,
                                                         'blog_authors': blog_authors,
                                                         },)
    
    return HttpResponseRedirect(reverse('blog.views.blog', args = (blog.name, )))

@login_required
def new_comment(request, name, id):
    blog = Blog.objects.get(name = name)
    post = Post.objects.get(id = id)
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            post.comments += 1
            post.save()
        else:
            return HttpResponse("Incorrect form!!")
    else:
        form = NewCommentForm({'post':post})
        all_comments = post.comment_set.all().order_by('-created')
        return render_to_response('blog/new_comment.html', {'form': form,
                                                            'post': post,
                                                            'blog': blog,
                                                            'comments': all_comments,})

    return HttpResponseRedirect(reverse('blog.views.blog', args = (blog.name, )))
