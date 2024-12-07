from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(unique=True, max_length=10, null=True, blank=True)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=12)
    user_role = models.IntegerField(default=1)
    user_gender = models.IntegerField(null=True, blank=True)
    user_avatar = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user_email