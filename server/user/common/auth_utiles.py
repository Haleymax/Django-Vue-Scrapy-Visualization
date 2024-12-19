import logging
from typing import Any

from django.core.exceptions import ObjectDoesNotExist

from user.models import User


def authenticate(email:str, password:str , result:dict[str:Any]) -> bool:
    try:
        user = User.objects.get(user_email=email)
        if password == user.user_password:
            result['status_code'] = 0
            result['message'] = 'login successful'
            return True
        else:
            result['status_code'] = 1
            result['message'] = 'wrong password'
            return False
    except ObjectDoesNotExist:
        result['status_code'] = 2
        result['message'] = 'user does not exist'
        return False