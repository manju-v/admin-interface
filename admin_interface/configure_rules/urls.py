from django.conf.urls import url
from django.contrib import admin
from configure_rules.views import *

urlpatterns = [
	url(r'^dashboard/$',dashboard)
]
