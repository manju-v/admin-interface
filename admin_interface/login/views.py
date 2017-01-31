from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from admin_interface import settings
from models import *
import datetime

# Create your views here.


@csrf_protect
def login(request):
	if(request.method == "POST"):
   		email = request.POST.get('email')
		password = request.POST.get('password')
		remember = request.POST.get('remember')
		if(check_user.password != password):
			return render(request,'login.html',{'error' : 'Incorrect password'})
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
	
@csrf_protect
def validate_email(request):
	email = request.GET.get('email')
	try:
		check_user = Login.objects.get(email=email)
		return HttpResponse('true')
	except Login.DoesNotExist:
		return HttpResponse('false')
	
#persistent cookie
def set_cookie(response, key, value, days_expire=7):
    max_age = days_expire * 24 * 60 * 60

    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                         "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires,
                        domain=SESSION_COOKIE_DOMAIN,
                        secure=None)

	#delete cookie on expire and logout
def delete_cookie(response, key):
    response.delete_cookie(key)
