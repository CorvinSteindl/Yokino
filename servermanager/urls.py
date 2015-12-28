from django.conf.urls import url, include
from django.contrib import admin
from .views import index, server, start_server, stop_server

urlpatterns = [
    url(r'^server/(?P<server_id>[0-9]+)/$', server, name='server'),
    url(r'server/(?P<server_id>[0-9]+)/start', start_server, name='start_server'),
    url(r'server/(?P<server_id>[0-9]+)/stop', stop_server, name='stop_server'),
    url(r'^', index, name='index')
]
