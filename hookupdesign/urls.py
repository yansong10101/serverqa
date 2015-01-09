from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'', include('designweb.urls', namespace='design', app_name='design')),
    # url(r'^index/', include('designweb.urls')),
    url(r'^maint/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, )
