from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50, blank=True, null=True)

    @property
    def name(self):
        if self.display_name:
            return self.display_name
        return self.user.username

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    """
    If a user is created, we create an user_account for that user
    """
    if created:
        UserAccount.objects.create(user=instance)
