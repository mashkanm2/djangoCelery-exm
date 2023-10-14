from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import userManagerObject

class userAcountModel(AbstractBaseUser,PermissionsMixin):
    user_name=models.TextField(max_length=30,unique=True)
    email=models.TextField(max_length=30,unique=True)
    fullname=models.TextField(max_length=50)
    phone_number=models.TextField(max_length=11,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects=userManagerObject()
    
    USER_NAME='user_name'
    REQUIRED_FIELDS=['email','phone_number']
    
    
    def __str__(self):
        return self.user_name
    
    @property
    def is_staff(self):
        return self.is_admin
