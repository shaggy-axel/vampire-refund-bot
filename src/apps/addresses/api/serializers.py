from typing import Optional
from rest_framework import serializers

from apps.addresses.models import Address, Country


class AddressRetrieveUpdateSerializer(serializers.ModelSerializer):
    using_now = serializers.SerializerMethodField()
    product_id = serializers.SerializerMethodField()

    class Meta:
        model = Address
        fields = (
            'id', 'name', 'line_1', 'line_2',
            'city', 'state', 'zip_code', 'phone',
            'status', 'used_by', 'used_at',
            'using_now', 'user_in_group',
            'country', 'product_id'
        )

    def get_using_now(self, obj: Address) -> bool:
        if obj.used_by:
            return bool(obj.used_by.current_address)
        return False

    def get_product_id(self, obj: Address) -> Optional[int]:
        try:
            return obj.product.id
        except Address.product.RelatedObjectDoesNotExist:
            return


class AddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'name', 'line_1', 'line_2',
            'city', 'state', 'zip_code', 'phone', 'country'
        )


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
