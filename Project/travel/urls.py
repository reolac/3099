from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^results/$', views.results, name='results'),
    url(r'^locations/$', views.cinema_locations, name='cinemalocs'),
    url(r'^cinemas/$', views.cinemas, name='cinemas'),
    url(r'^(?P<venue_id>[0-9]+)/$', views.detail, name='detail'),
]