from django.conf.urls.defaults import *

urlpatterns = patterns('links.views',
                       url(r'^(?P<name>.+)/new/$','new'),
                       url(r'^(?P<name>.+)', 'links'),
                       url(r'^$', 'links'),
                       )
