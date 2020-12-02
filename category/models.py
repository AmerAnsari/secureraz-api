from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.hashers import make_password


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    # def save(self, *args, **kwargs):
    #     self.name += 'd'
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def password_hash(self):
        return make_password(self.password)

    def __str__(self):
        return self.site
