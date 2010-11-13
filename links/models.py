from django.db import models

class Owner(models.Model):
    def __unicode__(self):
        return (self.name)

    name = models.TextField()

class Link(models.Model):
    def __unicode__(self):
        return (self.name)

    owner = models.ForeignKey(Owner)
    name = models.CharField(max_length = 60)
    content = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add = True)
    author =  models.CharField(max_length = 20)
