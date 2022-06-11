from rest_framework import viewsets

from apps.users.models import TelegramUser
from apps.users.api.serializers import (
    TelegramUserRetrieveSerializer,
    TelegramUserCreateSerializer,
    TelegramUserUpdateSerializer
)


class TelegramUserAPIViewSet(viewsets.ModelViewSet):
    queryset = TelegramUser.objects.all()
    lookup_field = 'telegram_id'
    filterset_fields = ['is_admin']

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return TelegramUserRetrieveSerializer
        elif self.request.method.lower() == 'post':
            return TelegramUserCreateSerializer
        elif self.request.method.lower() in ('put', 'patch'):
            return TelegramUserUpdateSerializer
        return TelegramUserRetrieveSerializer
