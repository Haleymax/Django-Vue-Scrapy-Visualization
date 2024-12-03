from django.db import models
from django.utils import timezone


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, default='male')
    age = models.IntegerField(default=0)
    avatar = models.CharField(max_length=50, default='/static/images/default_avatar.jpg')
    status = models.CharField(max_length=50, default='active')
    role = models.IntegerField(default=0)
    register_date = models.DateTimeField(default=timezone.now)
