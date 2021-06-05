from django.contrib import admin
from django.contrib import messages

from khazen.models import File


@admin.action(description='Unrelated files delete')
def delete_unrelated_files(modeladmin, request, queryset):
    references = File.objects.filter(media__isnull=True)
    deleted_files = 0
    for file in references:
        file.delete()
        deleted_files += 1
    if deleted_files != 0:
        messages.add_message(request, messages.INFO, f'{deleted_files} unrelated files has been deleted successfully.')
    else:
        messages.add_message(request, messages.ERROR, 'Not found any unrelated file.')


class FileActionAdmin(admin.ModelAdmin):
    list_display = ['filename', 'size_human', 'user_and_email']
    actions = [delete_unrelated_files]

    def user_and_email(self, obj):
        return f'{obj.user} ({obj.user.email})'


admin.site.register(File, FileActionAdmin)
