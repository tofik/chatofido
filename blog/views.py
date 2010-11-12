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
