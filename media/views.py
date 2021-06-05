from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from media.models import Media
from media.serializers import MediaSerializers, MediaWriteSerializers
from secureraz.utils import IsAuthAndOwner


class MediaViewSet(ModelViewSet):
    queryset = Media.objects.all()
    permission_classes = (IsAuthAndOwner,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MediaSerializers
        return MediaWriteSerializers

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
