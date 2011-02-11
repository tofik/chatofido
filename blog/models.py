from django.db import models
from django import forms

# Create your models here.

class Blog(models.Model):
    def __unicode__(self):
        return (self.name)
    name = models.TextField()
    modified = models.DateTimeField(auto_now = True)

class Post(models.Model):
    def __unicode__(self):
        return (self.title)
    blog = models.ForeignKey(Blog)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=20)

class Image(Post):
    def __unicode__ (self):
        return (self.title)
    image = models.ImageField(upload_to = "record/images")

class Comment(models.Model):
    def __unicode__(self):
        return (self.author)
    post = models.ForeignKey(Post)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length=20)



    # @models.permalink
    # def get_absolute_urls(self):
    #     return ('blog.views.details', [str(self.id)])


