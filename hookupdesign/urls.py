from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'', include('designweb.urls', namespace='design', app_name='design')),
                       # url(r'^index/', include('designweb.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
