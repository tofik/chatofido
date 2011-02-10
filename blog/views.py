from blog.models import Post, Blog, Image, Comment
from django.shortcuts import render_to_response, HttpResponseRedirect
from blog.forms import NewPostForm, NewImageForm, NewCommentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import datetime


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
        form = NewImageForm({'blog': blog})    
        return render_to_response('blog/new_image.html', {'form': form,
                                                    'blog': blog,
                                                    'blog_authors': blog_authors,
                                                    },)
    return HttpResponseRedirect(reverse('blog.views.blog', args = (blog.name, )))
        

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
        form = NewPostForm({'blog': blog})    
        return render_to_response('blog/new_post.html', {'form': form,
                                                    'blog': blog,
                                                    'blog_authors': blog_authors,
                                                    },)

    return HttpResponseRedirect(reverse('blog.views.blog', args = (blog.name, )))

def new_comment(request, name, id):
    blog = Blog.objects.get(name = name)
    post = Post.objects.get(id = id)
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
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

def blog(request, name = 'tofikowy'):
    blog = Blog.objects.get(name = name)
    all_blogs = Blog.objects.values('name').distinct()
    blog_authors = blog.post_set.values('author').distinct()
    all_authors = Post.objects.values('author').distinct()
    all_posts = blog.post_set.all().order_by('-created')
#    all_images = blog.image_set.values('image')

    return render_to_response('blog/list.html', {'blog': blog,
                                                 'blogs': all_blogs,
                                                 'blog_authors': blog_authors,
                                                 'all_authors': all_authors,
                                                 'posts': all_posts,
 #                                                'images': all_images,
                                                 'today': datetime.date.today().month,
                                                 },
                              )
