from rest_framework import viewsets

from apps.addresses.models import Address
from apps.addresses.api.serializers import (
    AddressRetrieveUpdateSerializer,
    AddressCreateSerializer
)


class AddressAPIViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    # queryset = Address.objects.filter(status="notused")

    def get_serializer_class(self):
        if self.request.method.lower() == 'post':
            return AddressCreateSerializer
        return AddressRetrieveUpdateSerializer
