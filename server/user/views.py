import json
import logging

from django.http import HttpResponse
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt

import common
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

@csrf_exempt
def send_verification_code(request):
    result = {}
    if request.method == "POST":
        try:

            if not request.body:
                raise ValueError("the request cannot be empty")

            user_email = request.POST.get('user_email', None)
            use_type = request.POST.get('use_type', None)

            if not user_email or not use_type:
                raise ValueError("the request must contain 'user_email' and 'use_type'")

            if '@' not in user_email:
                raise ValueError("the mailbox is incorrect formatted")

            email_client = common.mail.get_mail()
            email_client.set_type(use_type)
            email_client.send_mail(user_email)
            if email_client.result :
                logging.info("the verification code is sent successfully")
                result['message'] = "the verification code is sent successfully"
                result['status'] = 0

                cache.set(user_email, email_client.verify_code, timeout=1000)

            else:
                logging.info("the verification code is not sent successfully")
                result['message'] = "the verification code is not sent successfully"
                result['status'] = 1

        except Exception as e:
            logging.error(e)
            result['message'] = f"error:{e}"
        finally:
            return HttpResponse(json.dumps(result), content_type="application/json", status=200)
    else:
        result['message'] = "the request must be POST"
        result['status'] = 6
        return HttpResponse(json.dumps(result), content_type="application/json", status=405)

def register_user(request):
    message = {}
    if request.method == 'POST':
        try:

            # 从前端表单中提取用户信息
            email = request.POST.get('email')
            password = request.POST.get('password')
            verify_code = request.POST.get('verify_code')


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