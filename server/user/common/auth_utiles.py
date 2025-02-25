from typing import Any

from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist

from user.common.return_model import ReturnBase
from user.models import User


def authenticate(email:str, password:str , result:ReturnBase) -> bool:
    try:
        user = User.objects.get(user_email=email)
        if password == user.user_password:
            result.status = 0
            result.message= '登录成功'
            return True
        else:
            result.status = 1
            result.message = '密码错误'
            return False
    except ObjectDoesNotExist:
        result.status = 2
        result.message = '用户不存在'
        return False


def retrieve_password_by_email(email:str, verify_code, result:ReturnBase) -> tuple[bool, str]:
    try:
        cache_verify_code = cache.get(email)
        if cache_verify_code == verify_code:
            user = User.objects.get(user_email=email)
            result.status = 0
            result.message = '成功找回密码，请注意邮箱查收'
            return True, user.user_password
        else:
            result.status = 4
            result.message = "验证码不正确"
            return False, ""
    except ObjectDoesNotExist:
        result.status = 3
        result.message = '该用户不存在'
        return False, ''