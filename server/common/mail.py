import random
import os
import sys

from django.core.mail import send_mail
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

django.setup()
import smtplib


def send_verification_code(to_email:str) -> int:
    """
    发送邮箱验证码
    :param to_email: 目标邮箱地址
    :return: 成功返回 验证码 ，失败返回-1
    """
    sms_code = '%06d' % random.randint(1, 999999)
    EMAIL_FROM = 'captcha.test456@outlook.com'
    email_title = '验证码'
    emai_body = f"您的邮箱注册验证码为：{sms_code}，该验证码有效时间为两分钟，请及时进行验证。"
    send_status = send_mail(email_title, emai_body, EMAIL_FROM, [to_email])
    if send_status == 0 :
        return send_status
    else :
        return -1

def test2(to_email:str) -> int:
    """
    发送邮箱验证码
    :param to_email: 目标邮箱地址
    :return: 成功返回 验证码 ，失败返回-1
    """
    sms_code = '%06d' % random.randint(1, 999999)
    EMAIL_FROM = 'captcha.test456@outlook.com'
    email_title = '验证码'
    emai_body = f"您的邮箱注册验证码为：{sms_code}，该验证码有效时间为两分钟，请及时进行验证。"
    send_status = send_mail(email_title, emai_body, EMAIL_FROM, [to_email])
    if send_status == 0 :
        return send_status
    else :
        return -1

status = send_verification_code(to_email='huanghongweimax@163.com')
print(status)
