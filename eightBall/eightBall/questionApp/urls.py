from django.conf.urls import url
from django.contrib import admin

from .views import (
question_index,
question_create,
question_present,
question_submit,
)

urlpatterns = [
	url(r'^$', question_index, name='index'),
	url(r'^create/$', question_create, name='create'),
	url(r'^present/$', question_present, name='present'),
	url(r'^present/(?P<id>[0-9]+)$', question_present, name='present'),
	url(r'^submit/(?P<id>[0-9]+)/(?P<answer>[a-z]+)/$', question_submit, name='submit'),
]