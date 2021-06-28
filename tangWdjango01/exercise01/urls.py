from django.conf.urls import url
from django.conf.urls import URLPattern
from exercise01 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]