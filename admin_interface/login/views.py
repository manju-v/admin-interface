from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
# Create your views here.


@csrf_protect
def main(request):
    return render(request,'login.html')

