import json

from django.http import HttpResponse
from django.shortcuts import render

from common.mail import get_mail
from user import models

email_client = get_mail()

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_user(request):
    user = models.User(user_email='hongwei.huang@outlook.com',user_password='123456')
    user.save()
    return HttpResponse("ok")


def register_user(request):
    message = {}
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # 从前端表单中提取用户信息
            email = data.get('email')
            password = data.get('password')
            verify_code = data.get('verify_code')

            if not email :
                message['email'] = '邮箱不能为空'
            if not password :
                message['password'] = '密码不能为空'

            if len(password) < 8 or len(password) > 15:
                message['password'] = '密码长度不能低于8位或超过15位'
                return HttpResponse(json.dumps(message))

            if verify_code == email_client.verify_code:
                user = models.User(user_email=email,user_password=password)
                user.save()
                message['success'] = '注册成功'
                return HttpResponse(json.dumps(message), status=201)
            elif verify_code == '' :
                message['verify_code'] = '验证码不能为空'
            elif verify_code != email_client.verify_code:
                message['verify_code'] = '验证码不正确'

            return HttpResponse(json.dumps(message), status=400)

        except json.JSONDecodeError:
            return HttpResponse({'error' : '无效请求'}, status = 405)


    return HttpResponse({'error' : "无效请求，请检查发送表达"}, status = 405)