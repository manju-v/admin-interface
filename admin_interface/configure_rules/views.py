from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from admin_interface import settings
# Create your views here.


def dashboard(request):
	#if request.is_authenticated:
	return render(request,'dashboard.htm',{'is_authenticated' : 'true'})
	#else:
	#return HttpResponseRedirect('/')
	
