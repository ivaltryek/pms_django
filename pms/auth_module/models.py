from django.conf import settings
from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

# Create your models here.

class Teacher(models.Model):
    department = models.CharField(max_length=2, default ='')
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    contact = models.BigIntegerField(default = 0)

    def __str__(self):
        return self.user

class User(AbstractUser):
    department = models.CharField(max_length=2)
    contact = models.BigIntegerField()
    username = models.CharField(max_length=18,unique=True)
    def __str__(self):
        return self.username

