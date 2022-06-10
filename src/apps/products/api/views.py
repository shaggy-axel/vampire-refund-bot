from rest_framework.views import APIView, Response, status, Request

from apps.products.api.serializers import ProductSerializer
from apps.products.models import Product


class ProductAPIView(APIView):
    def get(self, request: Request):
        address = request.query_params.get("address", None)
        if address:
            product = Product.objects.filter(address__id=address).first()
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
