from django.conf.urls import patterns, url

from sharing import views

urlpatterns = patterns('',
    url(r'^(?P<root>[^:]*)$', views.admin, name='admin'),
    url(r'^(?P<root>[^:]*):(?P<token>[^/]*)(?P<sub>.*)$', views.sub, name='sub')
)
