from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# class Profile():

class MyUser(AbstractBaseUser):
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    REQUIRED_FIELDS = ["email", "first_name", "last_name", "password"] 

    def __str__(self):
        return (self.first_name + " " + self.last_name)