from rest_framework import serializers

from apps.addresses.models import Address


class AddressRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id', 'name', 'line_1', 'line_2', 'city', 'state',
            'zip_code', 'phone', 'status', 'used_by', 'used_at'
        )


class AddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'name', 'line_1', 'line_2',
            'city', 'state', 'zip_code', 'phone',
        )
