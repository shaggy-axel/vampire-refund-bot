from rest_framework import viewsets, views, response, status

from apps.addresses.models import Address
from apps.addresses.api.serializers import (
    AddressRetrieveUpdateSerializer,
    AddressCreateSerializer
)


class AddressAPIViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == 'post':
            return AddressCreateSerializer
        return AddressRetrieveUpdateSerializer


class GetAddressAPI(views.APIView):
    def get(self, request):
        # raise ValueError
        obj = Address.objects.filter(status='notused').first()
        data = AddressRetrieveUpdateSerializer(obj).data
        return response.Response(data, status.HTTP_200_OK)
