from django.http import HttpResponse
from django.shortcuts import render

from DVSV.server import models


# Create your views here.

def add_user(request):
    user = models.User.objects.create_user(id=1, email='hongwei.huang@unity.cn', password='209020357', user='haley', username='hongwei.huang', gender='male')
    user.save()
    return HttpResponse("<p> 添加用户成功 </p>")
