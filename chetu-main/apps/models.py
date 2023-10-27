from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from . manager import CustomManager
from django.conf import settings



# Create your models here.
class Users1(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    # author = models.ForeignKey(User,on_delete=models.CASCADE, default=None)



    
class CustomUser(AbstractUser):
    role_based = [
    ('FM', 'Floor Manager'),
    ('TL', 'Team Lead'),
    ('TM', 'Team Member'),
    ('TR', 'Trainee'),
]

    status = models.CharField(max_length=2, choices=role_based)

    objects=CustomManager()

    def __str__(self):
        return self.username
    


    