from django.contrib.auth.models import User
from django.db import models
import uuid


class FileType(models.IntegerChoices):
    IMAGE = 1
    DOCUMENT = 2
    COMPRESSED = 3
    AUDIO = 4
    VIDEO = 5
    OTHER = 6


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100, blank=True, null=True)
    file = models.FileField()
    file_type = models.IntegerField(choices=FileType.choices, default=FileType.OTHER)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.file.name = f'{self.uuid}' + '_' + f'{self.name}' + '_' + self.file.name
        if self.file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            self.file_type = FileType.IMAGE
        elif self.file.name.lower().endswith(('.pdf',)):
            self.file_type = FileType.DOCUMENT
        super().save(*args, **kwargs)
