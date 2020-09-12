from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {'insert_me':'Hello I am from login/index.html'}
    return render(request,'login/index.html',context=context)