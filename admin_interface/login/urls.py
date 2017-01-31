from django.conf.urls import url
from django.contrib import admin
from login.views import *

urlpatterns = [
	url(r'^$', login),
	url(r'^register.*$',register),
	url(r'^validate_email/$',validate_email)
]
