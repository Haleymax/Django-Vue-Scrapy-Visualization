import json
import logging

from django.db.models.expressions import result
from django.http import HttpResponse
from django.core.cache import cache
from django.views import View
from django.views.decorators.csrf import csrf_exempt

import common
from common.mail import get_mail
from data.menu import menu_data
from user import models
from user.common.auth_utiles import authenticate, retrieve_password_by_email
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
    """
    用于登录的接口
    """
    result = {}
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        ret = authenticate(email, password, result)
        if ret:
            request.session['email'] = email
            request.session.set_expiry(3600)
            return HttpResponse(json.dumps(result), status=201)
        else:
            return HttpResponse(json.dumps(result), status=201)
    else:
        result['status'] = 'fail'
        return HttpResponse(json.dumps(result), status=400)




@csrf_exempt
def send_verification_code(request):
    """
    用于发送验证码的接口
    """
    result = {}
    if request.method == "POST":
        try:

            if not request.body:
                raise ValueError("the request cannot be empty")

            user_email = request.POST.get('user_email', None)
            use_type = request.POST.get('use_type', None)

            if not user_email or not use_type:
                result['status'] = 0
                result['message'] = '邮箱地址不能为空'

            if '@' not in user_email:
                result['status'] = 2
                result['message'] = '邮箱地址格式不正确'

            if cache.get(user_email):
                result['status'] = 5
                result['message'] = '以发送请及时接收'
                return HttpResponse(json.dumps(result), status=201)

            email_client = common.mail.get_mail()
            email_client.connect()
            email_client.set_verification_code_type(use_type)
            email_client.create_verify_code_mail()
            email_client.send_mail(user_email)
            if email_client.result :
                logging.info("the verification code is sent successfully")
                result['message'] = "验证码发送成功"
                result['status'] = 0
                cache.set(user_email, email_client.verify_code, timeout=1000)
            else:
                logging.info("the verification code is not sent successfully")
                result['message'] = "验证码发送失败"
                result['status'] = 3

        except Exception as e:
            result['message'] = f"the verification code is not sent successfully:{e}"
            result['status'] = 3
        finally:
            return HttpResponse(json.dumps(result), content_type="application/json", status=201)
    else:
        result['message'] = "请求方式错误"
        result['status'] = 4
        return HttpResponse(json.dumps(result), content_type="application/json", status=405)

@csrf_exempt
def register(request):
    """
    用于注册的接口
    """
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

@csrf_exempt
def retrieve_password(request):
    """
    用于找回密码的接口
    """
    result = {}
    if request.method == 'POST':
        try:
            # 从前端表单中提取用户信息
            email = request.POST.get('email')
            verify_code = request.POST.get('verify_code')
            if not email or not verify_code:
                result['status'] = 1
                result['message'] = "必须填写邮箱和验证码"
                return HttpResponse(json.dumps(result), content_type="application/json", status=201)

            if '@' not in email:
                result['status'] = 2
                result['message'] = "邮箱地址的格式不正确"
                return HttpResponse(json.dumps(result), content_type="application/json", status=201)

            ret, db_password = retrieve_password_by_email(email=email, verify_code=verify_code, result=result)

            if not ret:
                return HttpResponse(json.dumps(result), content_type="application/json", status=201)
            else:
                email_client = common.mail.get_mail()
                email_client.connect()
                email_client.create_retrieve_password_mail(password=db_password)
                email_client.send_mail(recipient=email)
                if email_client.result :
                    result['status'] = 0
                    result['message'] = "邮件发送成功，请注意查收"
                    return HttpResponse(json.dumps(result), content_type="application/json", status=201)
                else:
                    result['status'] = 3
                    result['message'] = '邮件发送失败，请重试'
                return HttpResponse(json.dumps(result), content_type="application/json", status=201)

        except Exception as e:
            result['message'] = f"服务器异常，请重试"
            result['status'] = 4
        finally:
            return HttpResponse(json.dumps(result), content_type="application/json", status=201)
    else:
        result['message'] = "请求方式不正确"
        result['status'] = 5
        return HttpResponse(json.dumps(result), status = 405)


def menu(request):
    result = {}
    if request.method == 'GET':
        try:
            email = request.session.get('email')
            status = request.session.get('status')

            if not email or not status:
                result['status'] = 1
                result['message'] = '用户登录状态不正常'
                return HttpResponse(json.dumps(result), content_type="application/json", status=201)
            else:
                result['status'] = 0
                result['message'] = '返回菜单数据'
                result['data'] = menu_data
                return HttpResponse(json.dumps(result), content_type="application/json", status=201)
        except Exception as e:
            result['status'] = 2
            result['message'] = f"error:{e}"
    else:
        result['status'] = 3
        result['message'] = "请求方式有误"