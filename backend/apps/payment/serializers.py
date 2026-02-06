from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'id',
            'order',
            'method',
            'status',
            'amount',
            'transaction_id',
            'created_at',
        )
        read_only_fields = (
            'status',
            'transaction_id',
            'amount',
            'created_at',
        )


class PaymentReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'id',
            'method',
            'status',
            'amount',
            'transaction_id',
            'created_at',
        )
