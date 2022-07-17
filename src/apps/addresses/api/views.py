from rest_framework import viewsets, views, response, status
from rest_framework.request import Request

from apps.addresses.models import Address, Country
from apps.addresses.api.serializers import (
    AddressRetrieveUpdateSerializer,
    AddressCreateSerializer,
    CountrySerializer
)


class AddressAPIViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == 'post':
            return AddressCreateSerializer
        return AddressRetrieveUpdateSerializer


class GetAddressAPI(views.APIView):
    def get(self, request: Request) -> response.Response:
        country = request.query_params['country']
        obj = Address.objects.filter(status='notused', country=country)
        if obj:
            obj = obj.first()
            data = AddressRetrieveUpdateSerializer(obj).data
            return response.Response(data, status.HTTP_200_OK)
        return response.Response(
            {"error": f"does not exists address with status notused and country {country}"},
            status.HTTP_404_NOT_FOUND
        )


class GetUsedAddressesAPI(views.APIView):
    def get(self, request: Request) -> response.Response:
        obj = Address.objects.filter(status="used").exclude(product=None)
        return response.Response(
            AddressRetrieveUpdateSerializer(obj, many=True).data, status.HTTP_200_OK)


class GetCountriesAPIView(views.APIView):
    def get(self, request: Request) -> response.Response:
        queryset = Country.objects.all()
        return response.Response(
            CountrySerializer(queryset, many=True).data, status=status.HTTP_200_OK
        )
