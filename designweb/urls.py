from django.conf.urls import url, patterns
from designweb import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^test_page/', views.test_page, name='test_page'),
)
