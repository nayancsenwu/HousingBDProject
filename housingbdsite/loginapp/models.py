from django.db import models
# from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location="/media/profile_pics")


# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_id = models.URLField(blank=True)
    profile_pic = models.ImageField(storage=fs , blank=True)


    def __str__(self):
        return self.user.username