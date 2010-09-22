from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.TextField()

class Post(models.Model):
    blog = models.ForeignKey(Blog)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=20)

    # @models.permalink
    # def get_absolute_urls(self):
    #     return ('blog.views.details', [str(self.id)])


