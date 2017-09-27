from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^menu/$', views.menu),
    url(r'^reservation/$', views.reservation),
    url(r'^addreservation$', views.addreservation),
]