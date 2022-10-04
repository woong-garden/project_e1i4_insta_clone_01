from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import UserManager

# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(upload_to='')  # 프로필 이미지
    nickname = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=24, unique=True , default='')
    username = None
    
    USERNAME_FIELD = 'name'
    
    class Meta:
        db_table = "User"