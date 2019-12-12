from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.

class LoginValue(AbstractBaseUser):
    login = models.CharField(max_length=127, unique=True, null=False, blank=False)
    email = models.EmailField(null=False)
    first_name = models.CharField(max_length=127, null=True)
