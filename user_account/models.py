import humanize
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='user_account', on_delete=models.CASCADE)
    storage_limit = models.IntegerField(
        verbose_name="storage_limit",
        help_text="size of user storage",
        default=209715200
    )
    storage_current = models.IntegerField(
        verbose_name="storage_current",
        help_text="size of user storage",
        default=0
    )

    @property
    def storage_limit_human(self):
        return humanize.naturalsize(self.storage_limit)

    @property
    def storage_current_human(self):
        return humanize.naturalsize(self.storage_current)

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    """
    If a user is created, we create an user_account for that user
    """
    if created:
        UserAccount.objects.create(user=instance)
