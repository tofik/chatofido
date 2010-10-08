from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',

                       url(r'^list/$', 'list'),
                       url(r'^(?P<name>.+)/new/$','new'),
                       url(r'^(?P<name>.+)', 'blog'),

                       )
