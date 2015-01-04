from django.conf.urls import url
from designweb import views

urlpatterns = {
    url(r'^index/', views.index, name='index'),
    url(r'logout/', views.logout_view, name='logout'),
    url(r'login/', views.login_view, name='login'),
}
