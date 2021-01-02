from django.contrib.auth.models import User
from django.db import models

from khazen.models import File
from secureraz.encryption import Encryption


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    # photo = models.ForeignKey(File, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    password = Encryption(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.site
