from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('core.views',
    url(r'^$', views.index, name='index'),
    url(r'^frequency/$', views.frequency, name='frequency'),
    url(r'^test/$', views.test, name='test'),
)