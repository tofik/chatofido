from chatofido.links.models import Link
from django.forms import ModelForm

class NewLinkForm(ModelForm):
    class Meta:
        model = Link
        field = ('name', 'content', 'author')
