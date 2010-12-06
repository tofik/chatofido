from chatofido.blog.models import Post, Image
from django.forms import ModelForm
from django import forms

class NewPostForm(ModelForm):
    class Meta:
        model = Post
        field = ('content', 'title', 'author')

#to jest chyba wcale niepotrzebne

class NewImageForm(forms.Form):
#    url = forms.CharField(required=False)
    class Meta:
        model = Image
