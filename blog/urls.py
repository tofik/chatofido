from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
                       url(r'^(?P<name>.+)/new_post/$','new_post'),
                       url(r'^(?P<name>.+)/new_image/$','new_image'),
                       url(r'^(?P<name>.+)/(?P<id>.+)/new_comment/$', 'new_comment'),
                       url(r'^(?P<name>.+)/list/$', 'blog'),
                       url(r'^logout/$', 'logout_view'),
                       url(r"^$", 'blog'),
                       )
