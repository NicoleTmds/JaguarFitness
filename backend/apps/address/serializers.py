from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'street',
            'number',
            'district',
            'city',
            'state',
            'zip_code',
            'complement',
        )
        read_only_fields = ('id',)
