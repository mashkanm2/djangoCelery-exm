from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

class UserAccountModel(models):
    username=models.CharField(max_length=30,unique=True)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    phonenumber=models.CharField(max_length=12,unique=True)
    email=models.CharField(max_length=30,unique=True)
    is_active=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)


    USERNAME_FIELD='username'
    REQUIRED_FIELD=['phonenumber','email']

def __str__(self):
    return str(f"{self.firstname}-{self.lastname}")

@property
def is_staff(self):
    return self.is_admin



