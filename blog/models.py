from django.db import models

# Create your models here.

class Post(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20)
