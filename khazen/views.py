from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from khazen.models import File
from khazen.serializers import FileSerializers
from secureraz.utils import IsAuthAndOwner


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializers
    permission_classes = (IsAuthAndOwner,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['file_type']
    search_fields = ('name',)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
