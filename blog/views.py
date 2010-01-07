from blog.models import Post
from django.shortcuts import render_to_response

# Create your views here.

def list(request):
    all_posts=Post.objects.all()

    return render_to_response('blog/list.html', {'posts': all_posts})
