from django.conf.urls import url
from django.contrib import admin
from login.views import *

urlpatterns = [
	url(r'^main', main),
	url(r'^',register)
]
