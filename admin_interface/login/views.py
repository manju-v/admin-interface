from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from admin_interface import settings
from models import *
# Create your views here.


@csrf_protect
def main(request):
	if(request.method == "POST"):
   		username = request.POST.get('username')
		password = request.POST.get('password')
		remember = request.POST.get('remember')
		
		return render(request,'login.html')
	else:
		return render(request,'login.html')

@csrf_exempt
def register(request):
	context = RequestContext(request)
	if(request.method == "POST"):
		empid = request.POST.get('empid')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		confirm_pswd = request.POST.get('confirm-password')
		
		login = Login(emp_id=empid,emp_name=username,email=email,password=password)
		login.save()
		return HttpResponse("Sign up")
	else:
		return render_to_response(request,'register.html')
