from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
                       url(r'^(?P<name>.+)/new/$','new'),
                       url(r'^(?P<name>.+)', 'blog'),
                       url(r'^list/$', 'list'),
                       
                       )
