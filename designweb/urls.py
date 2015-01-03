from django.conf.urls import url
from designweb import views

urlpatterns = {
    url(r'^index/', views.index, name='index'),
}
