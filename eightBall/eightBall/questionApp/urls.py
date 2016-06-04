from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views

from .views import (
question_index,
question_create,
question_present,
question_submit,
login_page,
logout_page,
register,
register_success,
)

urlpatterns = [
	url(r'^$', question_index, name='index'),
	url(r'^create/$', question_create, name='create'),
	url(r'^present/$', question_present, name='present'),
	url(r'^present/(?P<id>[0-9]+)$', question_present, name='present'),
	url(r'^submit/(?P<id>[0-9]+)/(?P<answer>[a-z]+)/$', question_submit, name='submit'),
    url(r'^logout/$', logout_page, name='logout_page'),
	url(r'^accounts/login/$', login_page, name='login_page'),
    url(r'^register/$', register, name='register'),
    url(r'^register/success/$', register_success, name='register_success'),
]