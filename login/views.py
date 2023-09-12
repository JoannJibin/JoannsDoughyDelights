from django.shortcuts import render
from .models import login
# Create your views here.

def login(request):
 logins= login .objects. all()
 return render (request,'login.html',{'logins':login})