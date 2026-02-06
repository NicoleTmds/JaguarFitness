from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.shortcuts import get_object_or_404

from .models import Order, OrderItem
from .serializers import OrderSerializer
from apps.cart.views import get_or_create_cart
from apps.address.models import Address


class OrderViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        Lista todos os pedidos do usuário
        """
        orders = Order.objects.filter(
            user=request.user
        ).order_by('-created_at')

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Detalhe de um pedido específico
        """
        order = get_object_or_404(
            Order,
            id=pk,
            user=request.user
        )

        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    
    @transaction.atomic
    def create(self, request):
        """
        Checkout:
        - cria o pedido
        - cria os itens
        - snapshot do endereço
        - NÃO limpa o carrinho
        """

        address_id = request.data.get('address')

        if not address_id:
            return Response(
                {'detail': 'Address is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        address = get_object_or_404(
            Address,
            id=address_id,
            user=request.user
        )

        cart = get_or_create_cart(request)
        cart_items = cart.items.all()

        if not cart_items.exists():
            return Response(
                {'detail': 'Cart is empty'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Criação do pedido com SNAPSHOT do endereço
        order = Order.objects.create(
            user=request.user,
            status='pending',
            total_amount=0,

            street=address.street,
            number=address.number,
            district=address.district,
            city=address.city,
            state=address.state,
            zip_code=address.zip_code,
            complement=address.complement,
        )

        total = 0

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                unit_price=item.product.price
            )

            total += item.quantity * item.product.price

        order.total_amount = total
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def cancel(self, request, pk=None):
        order = get_object_or_404(
            Order,
            id=pk,
            user=request.user
        )

        if order.status != 'pending':
            return Response(
                {'detail': 'Order cannot be canceled'},
                status=status.HTTP_400_BAD_REQUEST
            )

        order.status = 'canceled'
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
