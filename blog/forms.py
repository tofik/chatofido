from chatofido.blog.models import Post
from django.forms import ModelForm
from django import forms

class NewPostForm(ModelForm):
    class Meta:
        model = Post
#        field = ('content', 'title', 'author')


# class NewFileForm(forms.Form):
#     title = forms.CharField(max_length = 50)
#     filename = forms.FileField()
