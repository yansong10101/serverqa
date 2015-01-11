from django.conf.urls import url, patterns, include
from designweb import views
from rest_framework import routers

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^signup/', views.signup, name='signup'),
)


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns += patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)