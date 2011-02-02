from chatofido.blog.models import Post, Image, Comment
from django.forms import ModelForm
from django import forms

class NewPostForm(ModelForm):
    class Meta:
        model = Post
        field = ('content', 'title', 'author')

#to jest chyba wcale niepotrzebne

class NewImageForm(forms.ModelForm):
#    url = forms.CharField(required=False)
    class Meta:
        model = Image

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        field = ('content', 'author', 'created')
