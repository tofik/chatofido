from chatofido.blog.models import Post
from django.forms import ModelForm

class NewPostForm(ModelForm):
    class Meta:
        model = Post
        field = ('content', 'author')

