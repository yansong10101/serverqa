from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hookupdesign.views.home', name='home'),
    url(r'^index/', include('designweb.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
