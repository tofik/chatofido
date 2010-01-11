from django.conf.urls.defaults import *
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r"^blog/", include("blog.urls")),

    # Admin urls
                       (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       (r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns("django.views",
                            url(r"^templates/(?P<path>.*)", 
                                "static.serve", 
                                { "document_root": settings.MEDIA_ROOT,
                                  'show_indexes': True })   
                            )
