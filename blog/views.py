from blog.models import Post
from django.shortcuts import render_to_response
from blog.forms import NewPostForm

# Create your views here.

def list(request):
    all_posts=Post.objects.all()

    return render_to_response('blog/list.html', {'posts': all_posts})

def new(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/blog/list/')

    else:
        form = NewPostForm()
        
    return render_to_response('blog/new.html', {'form': form})
