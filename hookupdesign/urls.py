from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'', include('designweb.urls', namespace='design', app_name='design')),
    # url(r'^index/', include('designweb.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns(
    '',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)