from django.contrib.auth.models import User
from django.db import models

from khazen.models import File


class Media(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1024, blank=True, null=True)
    file = models.ForeignKey(File, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(
        'category.Category',
        related_name='medias',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> models.CharField:
        return self.name
