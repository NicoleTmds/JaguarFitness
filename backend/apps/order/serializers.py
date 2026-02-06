from rest_framework import serializers
from .models import Order, OrderItem
from apps.payment.serializers import PaymentReadSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(
        source='product.name',
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = (
            'id',
            'product',
            'product_name',
            'quantity',
            'unit_price',
        )


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    payments = PaymentReadSerializer(many=True, read_only=True)
    
    # Endereço (snapshot)
    address = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = (
            'id',
            'status',
            'total_amount',
            'items',
            'payments',
            'address',
            'created_at',
        )

    def get_address(self, obj):
        return {
            'street': obj.street,
            'number': obj.number,
            'district': obj.district,
            'city': obj.city,
            'state': obj.state,
            'zip_code': obj.zip_code,
            'complement': obj.complement,
        }