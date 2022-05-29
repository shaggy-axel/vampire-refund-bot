from rest_framework import serializers

from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "shop_name", "price", "delivery_date", "address")

    def create(self, validated_data):
        return super().create(validated_data)
