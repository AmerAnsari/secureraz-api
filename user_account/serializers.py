from django.contrib.auth.models import User
from rest_framework import serializers

from user_account.models import UserAccount


class UserAccountSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()

    class Meta:
        model = UserAccount
        fields = (
            'display_name',
            'name',
        )
        extra_kwargs = {
            'display_name': {'write_only': True},
        }


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    user_account = UserAccountSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'date_joined',
            'last_login',
            'user_account',
            'password',
        )
        extra_kwargs = {
            'date_joined': {'read_only': True},
            'last_login': {'read_only': True},
            'password': {'write_only': True},
        }

    def create(self, validated_data: dict):
        return User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )
