from django.shortcuts import render
from .models import menu

def menu(request):
    menus= menu . objects. all()
    return render(request,'Menu.html',{'menus':menu})

    