from blog.models import Post, Blog
from django.shortcuts import render_to_response, HttpResponseRedirect
from blog.forms import NewPostForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import datetime

# Create your views here.

# def list(request):
#     all_posts = Post.objects.all().order_by('-created')
#     all_authors = Post.objects.values('author').distinct() 

#     return render_to_response('blog/list.html', {'posts': all_posts, 
#                                                  'authors': all_authors})


def new(request, name):
    blog = Blog.objects.get(name = name)
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = blog
            post.save()
        else:
            return HttpResponse("form is invalid or incomplete!!")
        
    else:
        blog_authors = Post.objects.values('author').distinct()
        form = NewPostForm({'blog': blog})    
        return render_to_response('blog/new.html', {'form': form,
                                                    'blog': blog,
                                                    'blog_authors': blog_authors,
                                                    },)

    return HttpResponseRedirect(reverse('blog.views.blog', args = (blog.name, )))
    
def blog(request, name):
    blog = Blog.objects.get(name = name)
    all_authors = Post.objects.values('author').distinct()
    blog_authors = blog.post_set.values('author').distinct()
    created_today = blog.post_set.filter(created__startswith = datetime.date.today())
    created_month = blog.post_set.filter(created__month = datetime.date.today().month)
    all_posts = blog.post_set.all().order_by('-created')

    return render_to_response('blog/list.html', {'blog': blog,
                                                 'blog_authors': blog_authors,
                                                 'posts': all_posts,
                                                 'created_today': created_today,
                                                 'created_this_month': created_month,
                                                 'today': datetime.date.today().month,
                                                 },
                              )
