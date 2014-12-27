from django.conf.urls import url
from designweb import views

urlpatterns = {
    url(r'^$', views.index, name='index'),
}
