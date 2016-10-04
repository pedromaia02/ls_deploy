from django.conf.urls import url

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	dre,
	)

urlpatterns = [
	url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete, name='delete'),
	url(r'^dre/$', dre, name='dre'),
	url(r'^dados/(?P<local>[\w\-]+)/$', post_detail, name='detail'),
]
