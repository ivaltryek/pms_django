from django.contrib import admin
from .models import Teacher
from django.contrib.auth import get_user_model
User = get_user_model()
# Register your models here.
admin.site.register(Teacher)
admin.site.register(User)

