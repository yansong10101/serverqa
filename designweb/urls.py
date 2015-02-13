from django.conf.urls import url, patterns, include
from designweb import views
from rest_framework import routers

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^user-profile/(?P<pk>[0-9]+)/$', views.user_profile, name='user-profile'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.product_view, name='product-view'),
    url(r'^cart/(?P<pk>[0-9]+)/$', views.my_cart, name='my-cart'),

    url(r'^api/products/$', views.ProductsList.as_view(), name='product-list'),
    url(r'^api/products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='product-detail'),
)


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns += patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)