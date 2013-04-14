from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^blog/', include('apps.blog.urls')),
    url(r'^', include('apps.page.urls')),
    url(r'^', include('django.contrib.flatpages.urls')),

)

# Static files url patterns
urlpatterns += staticfiles_urlpatterns()

# Media files url patterns
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/').rstrip('/'), 
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}
        )
   )
