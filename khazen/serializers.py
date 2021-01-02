from rest_framework import serializers

from khazen.models import File


class FileSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = File
        fields = (
            'uuid',
            'user',
            'name',
            'description',
            'file',
            'file_type',
        )
        read_only_fields = ('file_type',)
