from rest_framework import serializers

from apps.users.models import TelegramUser


class TelegramUserRetrieveSerializer(serializers.ModelSerializer):
    using_now = serializers.SerializerMethodField()

    class Meta:
        model = TelegramUser
        fields = ('telegram_id', 'username', 'using_now', 'current_address')

    def get_using_now(self, obj):
        return bool(obj.current_address)


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
        fields = ('current_address',)
