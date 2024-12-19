import json
import logging

from django.db.models.expressions import result
from django.http import HttpResponse
from django.core.cache import cache
from django.views import View
from django.views.decorators.csrf import csrf_exempt

import common
from common.mail import get_mail
from user import models
from user.common.auth_utiles import authenticate
from user.models import User

email_client = get_mail()

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_user(request):
    user = models.User(user_email='hongwei.huang@outlook.com',user_password='123456')
    user.save()
    return HttpResponse("ok")

@csrf_exempt
def login_user(request):
    result = {}
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        ret = authenticate(email, password, result)
        if ret:
            request.session.set_test_cookie()
            return HttpResponse(json.dumps(result), status=201)
        else:
            return HttpResponse(json.dumps(result), status=201)
    else:
        result['status'] = 'fail'
        return HttpResponse(json.dumps(result), status=400)




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

@csrf_exempt
def register(request):
    result = {}
    if request.method == 'POST':
        try:
            # 从前端表单中提取用户信息
            email = request.POST.get('email')
            password = request.POST.get('password')
            verify_code = request.POST.get('verify_code')

            cache_verify_code = cache.get(email)

            # 验证邮箱和密码格式
            if not email or not password or not verify_code:
                raise ValueError("The request must contain email, password, and verify_code.")
            if len(password) < 8 or len(password) > 15:
                raise ValueError("Password length must be between 8 and 15 characters.")

            # 从缓存中获取验证码
            cached_verify_code = cache.get(email)
            if cached_verify_code is None or cached_verify_code != verify_code:
                raise ValueError("The verification code is incorrect or has expired.")

            if verify_code == cache_verify_code:
                user = models.User(user_email=email,user_password=password)
                user.save()
                result['success'] = '注册成功'
                result['status'] = 0

        except ValueError as e:
            result['message'] = f"error:{e}"
            result['status'] = 3
        except Exception as e:
            result['message'] = f"error:{e}"
            result['status'] = 5
            return HttpResponse(json.dumps(result), content_type="application/json", status=400)
        finally:
            return HttpResponse(json.dumps(result), content_type="application/json", status=201)
    else:
        result['message'] = "the request must be POST"
        result['status'] = 4
        return HttpResponse(json.dumps(result), status = 405)