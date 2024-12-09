import random
import smtplib
import time
from datetime import datetime

from email.mime.text import MIMEText
from email.header import Header
from config.read_config import app_config

email_config = app_config['email']

message_type = {
    'register' : "这是您用于注册的验证码: ",
    'forget' : "这是您用于找回密码的验证码: "
}

class Mail:
    def __init__(self):
        self.send_message = None
        self.smtp_server =  email_config['server']
        self.port = email_config['port']
        self.sender = email_config['sender']
        self.password = email_config['password']
        self.send_time = None
        self.verify_code = 0
        self.message = None
        self.recipient_email = None
        self.result = None

    def set_type(self, use_type):
        self.message = message_type[use_type]

    def create_mail(self):
        self.generate_verify_code()
        self.message += self.verify_code
        self.send_message = MIMEText(self.message, 'plain', 'utf-8')
        self.send_message['From'] = Header(self.sender, 'utf-8')
        self.send_message['To'] = Header(self.recipient_email, 'utf-8')
        self.send_message['Subject'] = Header('验证码', 'utf-8')

    def send_mail(self, recipient):
        try:
            # 连接邮件服务器并登录
            self.recipient_email = recipient
            smtp_connection = smtplib.SMTP(self.smtp_server, self.port)
            smtp_connection.login(self.sender, self.password)
            self.create_mail()

            # 发送验证码
            smtp_connection.sendmail(self.sender, self.recipient_email, self.send_message.as_string())
            now = datetime.now()
            self.send_time = int(time.mktime(now.timetuple()))

            smtp_connection.quit()
            self.result = True
        except Exception as e:
            print(e)
            self.result = False

    def generate_verify_code(self):
        random_list = list(map(lambda x:random.randint(0,9), [y for y in range(6)]))
        self.verify_code = "".join('%s' % i for i in random_list)

def get_mail():
    return Mail()