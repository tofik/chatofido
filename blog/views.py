from blog.models import Post
from django.shortcuts import render_to_response, HttpResponseRedirect
from blog.forms import NewPostForm

# Create your views here.

def list(request):
    all_posts = Post.objects.all().order_by('-created')
    all_authors = Post.objects.values('author').distinct() 

    return render_to_response('blog/list.html', {'posts': all_posts, 
                                                 'authors': all_authors})

def new(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog/list/')

    else:
        form = NewPostForm()
        
    return render_to_response('blog/new.html', {'form': form})

def blog(request, name):
    blog = Blog.objects.get(name = name)

    return render_to_response({'blog': blog})
