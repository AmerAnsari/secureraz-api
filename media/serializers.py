from rest_framework import serializers

from category.serializers import CategorySerializers
from khazen.serializers import FileSerializers
from media import models
from media.models import Media


class MediaSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    file = FileSerializers()

    class Meta:
        model = Media
        fields = (
            'id',
            'name',
            'description',
            'file',
            'category',
            'created',
            'updated',
        )


class MediaWriteSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Media
        fields = (
            'id',
            'user',
            'name',
            'description',
            'file',
            'category',
            'created',
            'updated',
        )

    def to_representation(self, instance: models.File) -> dict:
        return MediaSerializers(instance).data
