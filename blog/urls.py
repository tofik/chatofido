from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
                       url(r'^(?P<name>.+)/new_post/$','new_post'),
                       url(r'^(?P<name>.+)/new_image/$','new_image'),
                       url(r'^(?P<name>.+)', 'blog'),
                       url(r"^", 'blog'),
                       )
