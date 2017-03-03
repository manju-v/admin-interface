from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from admin_interface import settings
from shared.redis_connection import get_connection
import json
# Create your views here.

@csrf_protect
def default_rule(request):
	#if request.is_authenticated:
	
	return render(request,'default_rule.htm',{'is_authenticated' : 'true'})
	#else:
	#return HttpResponseRedirect('/')
	
@csrf_protect
def get_redis_rules(request):
	if(request.method == "POST"):
		
		rules = []
		r = get_connection('default')
		rules = r.zrange('ruleset',0,-1,withscores=True)
		print (rules);
		return HttpResponse(json.dumps(rules),content_type = 'application/json')

	
