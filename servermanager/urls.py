from django.conf.urls import include, url
from django.contrib import admin

from .views import index, params_server, server, start_server, stop_server

urlpatterns = [
    url(r'^server/(?P<server_id>[0-9]+)/$', server, name='server'),
    url(r'server/(?P<server_id>[0-9]+)/start', start_server, name='start_server'),
    url(r'server/(?P<server_id>[0-9]+)/stop', stop_server, name='stop_server'),
    url(r'server/(?P<server_id>[0-9]+)/params', params_server, name='params_server'),
    url(r'^', index, name='index')
]
