from rest_framework.viewsets import ModelViewSet

from category.models import Category, Account
from category.serializers import CategorySerializers, AccountSerializers, AccountWriteSerializers
from secureraz.utils import IsAuthAndOwner


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = (IsAuthAndOwner,)
    search_fields = ('name',)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    permission_classes = (IsAuthAndOwner,)
    search_fields = ('name',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AccountSerializers
        return AccountWriteSerializers

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
