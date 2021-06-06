import uuid

import humanize
from django.contrib.auth.models import User
from django.db import models
# from magic.magic import Magic
from khazen import config
from khazen.utils import gen_filename
from secureraz.utils import IdName


class FileType(models.IntegerChoices):
    IMAGE = 1
    DOCUMENT = 2
    COMPRESSED = 3
    AUDIO = 4
    VIDEO = 5
    OTHER = 6


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    filename = models.CharField(verbose_name="file name", max_length=128, blank=True)
    file = models.FileField(verbose_name="file", upload_to=gen_filename)
    ext = models.CharField(verbose_name="ext", help_text="file mime-type", max_length=128, blank=True)
    size = models.IntegerField(verbose_name="size", help_text="size of file in Megabyte", default=0)
    type = models.IntegerField(choices=FileType.choices, default=FileType.OTHER)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'
        ordering = ('-uuid',)

    def __str__(self) -> str:
        return f"{self.filename} ({self.ext})"

    @property
    def file_type(self) -> object:
        return IdName(self.type, FileType).get_id_name()

    @property
    def size_human(self) -> object:
        return humanize.naturalsize(self.size)

    def save(self, *args, **kwargs):

        """Before save, get the original file Ext/mime-type using libmagic."""
        self.filename = self.file.name
        self.size = self.file.size
        # f = Magic(mime=True)
        # self.ext = f.from_buffer(self.file.file.read(2048))

        """Check the file size"""
        if (self.size / 1024) / 1024 > config.MAX_FILE_SIZE_ALLOWED:
            raise ValueError("File is larger than allowed ({:.1f} MB).".format(config.MAX_FILE_SIZE_ALLOWED))

        """Check the user storage"""
        user_storage_limit = self.user.user_account.storage_limit
        user_storage_current = self.user.user_account.storage_current + self.size

        if user_storage_current > user_storage_limit:
            raise ValueError("Your storage is full.")
        else:
            self.user.user_account.storage_current = user_storage_current
            self.user.user_account.save()

        """Set the file type"""
        # Image
        if self.file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            self.type = FileType.IMAGE

        # Document
        elif self.file.name.lower().endswith(
                ('.txt', '.pdf', '.ppt', '.pptx', '.doc', '.docx', '.html', '.htm', '.odt', '.ods', '.xls', '.xlsx')):
            self.type = FileType.DOCUMENT

        # Video
        elif self.file.name.lower().endswith(('.mp4', '.mov', '.wmv', '.flv', '.avi', '.avchd', '.webm', '.mkv')):
            self.type = FileType.VIDEO

        # Audio
        elif self.file.name.lower().endswith(
                ('.mp3', '.pcm', '.wav', '.aiff', '.aac', '.ogg', '.wma', '.flac', '.alac')):
            self.type = FileType.AUDIO

        # Compressed
        elif self.file.name.lower().endswith(
                ('.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip')):
            self.type = FileType.COMPRESSED

        # Others
        else:
            self.type = FileType.OTHER
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Update the user storage"""
        self.user.user_account.storage_current -= self.size
        self.user.user_account.save()
        super().delete(*args, **kwargs)


