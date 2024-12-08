import json

from django.http import HttpResponse
from django.shortcuts import render

from user import models


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_user(request):
    user = models.User(user_email='hongwei.huang@outlook.com',user_password='123456')
    user.save()
    return HttpResponse("ok")


def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse({'error' : '无效请求'}, status = 400)


    return HttpResponse({'error' : "无效请求，请检查发送表达"}, status = 405)