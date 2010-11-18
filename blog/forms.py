from chatofido.blog.models import Post, FilePost
from django.forms import ModelForm
from django import forms

class NewPostForm(ModelForm):
    class Meta:
        model = Post
        field = ('content', 'title', 'author')

class NewFileForm(ModelForm):
    class Meta:
        model = FilePost
        field = ('title', 'filename')

# class NewFileForm(forms.Form):
#     title = forms.CharField(max_length = 50)
#     filename = forms.FileField()
