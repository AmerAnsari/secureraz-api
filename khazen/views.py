from rest_framework.viewsets import ModelViewSet

from khazen.models import File
from khazen.serializers import FileSerializers
from secureraz.utils import IsAuthAndOwner


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    permission_classes = (IsAuthAndOwner,)
    serializer_class = FileSerializers

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
