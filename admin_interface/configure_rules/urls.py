from django.conf.urls import url
from django.contrib import admin
from configure_rules.views import *

urlpatterns = [
	url(r'^default_rule/$',default_rule),
	url(r'^get_redis_rules/$',get_redis_rules)
]
