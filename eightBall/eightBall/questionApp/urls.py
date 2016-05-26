from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login

from .views import (
question_index,
question_create,
question_present,
question_submit,
new_user,
)

urlpatterns = [
	url(r'^$', question_index, name='index'),
	url(r'^newuser/$', new_user, name='new_user'),
	url(r'^create/$', question_create, name='create'),
	url(r'^present/$', question_present, name='present'),
	url(r'^login/$', login),
	url(r'^present/(?P<id>[0-9]+)$', question_present, name='present'),
	url(r'^submit/(?P<id>[0-9]+)/(?P<answer>[a-z]+)/$', question_submit, name='submit'),
]