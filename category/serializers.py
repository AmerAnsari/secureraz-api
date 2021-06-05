from rest_framework import serializers

from category.models import Category, Account


class CategorySerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    accounts_count = serializers.ReadOnlyField()
    medias_count = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = (
            'id',
            'user',
            'name',
            'accounts_count',
            'medias_count',
        )


class AccountSerializers(serializers.ModelSerializer):
    category = CategorySerializers()

    class Meta:
        model = Account
        fields = (
            'id',
            'site',
            'username',
            'password',
            'category',
        )


class AccountWriteSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    site = serializers.CharField(
        help_text='This field will be your account website or app.',
    )
    username = serializers.CharField(
        help_text='This field will be your account username or email.',
    )

    class Meta:
        model = Account
        fields = (
            'id',
            'user',
            'site',
            'username',
            'password',
            'category',
        )

    def to_representation(self, instance):
        return AccountSerializers(instance).data
