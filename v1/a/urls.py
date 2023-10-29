"""
URL configuration for p1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse,request
from . import views


urlpatterns = [
    path('home.html',views.home),
    path('about.html',views.about),
    path('contact.html',views.contact),
    path('project.html',views.project),  
    path('add/<int:x>/<int:y>',views.add),
    path('sub/<int:x>/<int:y>',views.sub),
    path('mul/<int:x>/<int:y>',views.mul),
    path('div/<int:x>/<int:y>',views.div),
    path('a/<int:x>/<int:y>',views.a),
    path('s/<int:x>/<int:y>',views.s),
    path('s/<int:x>/<int:y>',views.m),
    path('s/<int:x>/<int:y>',views.d),
    path('shorturl/<str:url>',views.shorturl,name='shorturl'),
]