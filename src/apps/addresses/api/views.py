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
        obj = Address.objects.filter(status='notused')
        if obj:
            obj = obj.first()
            data = AddressRetrieveUpdateSerializer(obj).data
            return response.Response(data, status.HTTP_200_OK)
        return response.Response(
            {"error": "does not exists `not used` address"},
            status.HTTP_404_NOT_FOUND
        )
