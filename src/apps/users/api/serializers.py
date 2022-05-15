from rest_framework import serializers

from apps.users.models import TelegramUser


class TelegramUserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ('telegram_id',)


class TelegramUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = (
            'telegram_id',
            'username',
            'first_name',
            'last_name',
        )


class TelegramUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ('username',)
