from cgitb import html
from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Meher'})
def add(request):
    val1 = request.POST['num1']
    val2 = int(request.POST['num2'])
    

    return render(request,'result.html')



    