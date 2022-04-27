from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.fullname