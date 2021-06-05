from rest_framework import serializers

from khazen.models import File


class FileSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = File
        fields = ('uuid', 'file', 'filename', 'ext', 'size', 'size_human', 'file_type', 'user')
        read_only_fields = ('uuid', 'filename', 'ext', 'size', 'size_human', 'file_type', 'user')
