from django.contrib.auth.models import User
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from secureraz.utils import IsAuthAndOwnerOrReadOnly
from user_account.models import UserAccount
from user_account.serializers import UserSerializer, UserAccountSerializer


class UserViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class UserAccountViewSet(UpdateModelMixin, GenericViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    permission_classes = (IsAuthAndOwnerOrReadOnly,)
    lookup_field = 'user__username'
