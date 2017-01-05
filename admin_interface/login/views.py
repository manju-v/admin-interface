from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from admin_interface import settings
from models import *
import re
# Create your views here.


@csrf_protect
def login(request):
	if(request.method == "POST"):
   		username = request.POST.get('username')
		password = request.POST.get('password')
		remember = request.POST.get('remember')
		try:
			check_user = Login.objects.get(email=username)
		except Login.DoesNotExist:
			return render(request,'login.html',{'error' : 'User do not exist'})
		
		if(check_user.password == password):
			return HttpResponse("login successful")
	else:
		return render(request,'login.html')

@csrf_protect
def register(request):
	if(request.method == "POST"):
		empid = request.POST.get('empid')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		confirm_pswd = request.POST.get('confirm-password')												   
		login = Login(emp_id=empid,emp_name=username,email=email,password=password)
		login.save()
		return HttpResponseRedirect('/')
	else:
		return render(request,'register.html')
