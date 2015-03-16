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
    # Change Password URLs:
    url(r'^accounts/password_change/$',
        'django.contrib.auth.views.password_change',
        {'post_change_redirect': '/accounts/password_change/done/'},
        name="password_change"),
    (r'^accounts/password_change/done/$', 'django.contrib.auth.views.password_change_done'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
