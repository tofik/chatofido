from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
                       url(r'^(?P<name>.*)', 'blog'),
                       url(r'^list/$', 'list'),
                       url(r'^new/$','new'),
                       )
