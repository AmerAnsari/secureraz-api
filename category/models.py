from django.contrib.auth.models import User
from django.db import models

from khazen.models import File
from secureraz.encryption import Encryption


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    # photo = models.ForeignKey(File, null=True, blank=True, on_delete=models.SET_NULL)

    @property
    def accounts_count(self) -> int:
        return self.accounts.count()

    @property
    def medias_count(self) -> int:
        return self.medias.count()

    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    # password = Encryption(max_length=500)
    password = models.CharField(max_length=500)
    category = models.ForeignKey(Category, related_name='accounts', on_delete=models.CASCADE)

    def __str__(self):
        return self.site
