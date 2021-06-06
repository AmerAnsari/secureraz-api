from django.contrib import admin

from user_account.models import UserAccount


class Actions(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_superuser']

    def username(self, obj):
        return f'{obj.user.username}'

    def email(self, obj):
        return f'{obj.user.email}'

    def is_superuser(self, obj):
        return obj.user.is_superuser


admin.site.register(UserAccount, Actions)
