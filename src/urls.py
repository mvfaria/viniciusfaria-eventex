from django.conf.urls import patterns, include, url
from .core.views import Homepage

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings

admin.autodiscover()


urlpatterns = patterns('src',
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(r'^inscricao/', include('src.subscriptions.urls', namespace='subscriptions')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('src.core.urls', namespace='core')),
)

if settings.DEBUG is False:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.STATIC_ROOT}),
    )
