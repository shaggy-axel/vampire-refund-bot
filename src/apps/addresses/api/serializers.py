from rest_framework import serializers

from apps.addresses.models import Address


class AddressRetrieveUpdateSerializer(serializers.ModelSerializer):
    using_now = serializers.SerializerMethodField()

    class Meta:
        model = Address
        fields = (
            'id', 'name', 'line_1', 'line_2',
            'city', 'state', 'zip_code', 'phone',
            'status', 'used_by', 'used_at',
            'using_now', 'user_in_group'
        )

    def get_using_now(self, obj: Address) -> bool:
        if obj.used_by:
            return bool(obj.used_by.current_address)
        return False


class AddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'name', 'line_1', 'line_2',
            'city', 'state', 'zip_code', 'phone',
        )
