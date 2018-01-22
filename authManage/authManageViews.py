from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db import connection

def index(request):
    return render_to_response('authManage/index.html')

def login(request):
    return render_to_response('authManage/login.html')
