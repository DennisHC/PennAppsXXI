from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from datetime import datetime

class MyUser(AbstractBaseUser):
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    REQUIRED_FIELDS = ["email", "first_name", "last_name", "password"] 

    def __str__(self):
        return (self.first_name + " " + self.last_name)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    gender = models.BooleanField(default=True) # Girl = True; Boy = False
    reveal_time = models.DateTimeField()

    def __str__(self):
        return self.user