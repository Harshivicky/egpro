from django.shortcuts import render
from django.http import HttpResponse,request
import pyshorteners

def home(request):
    d={'Name':'vicky',
       'Age':'23',
       'Empid':1234}
    return render(request, 'home.html',d)
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def project(request):
    return render(request,'project.html')
def add(request,x,y):
    x1=x+y
    return HttpResponse(x1)
def sub(request,x,y):
    x1=x-y
    return HttpResponse(x1)
def mul(request,x,y):
    x1=x*y
    return HttpResponse(x1)
def div(request,x,y):
    x1=x/y
    return HttpResponse(x1)
def a(request,x,y):
    result=x+y
    return render(request,'result.html',{'result':result})
def s(request,x,y):
    result=x-y
    return render(request,'result.html',{'result':result})
def m(request,x,y):
    result=x*y
    return render(request,'result.html',{'result':result})
def d(request,x,y):
    result=x/y
    return render(request,'result.html',{'result':result})
def shorturl(request,url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.chilpit.short(url)
    return HttpResponse(f'Shortened URL: <a href="{shortened_url}">{shortened_url}</a>')
 
