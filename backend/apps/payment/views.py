from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import transaction
import uuid

from .models import Payment
from .serializers import PaymentSerializer
from apps.order.models import Order
from apps.cart.models import Cart


class PaymentViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def _order_has_address_snapshot(self, order):
        required_fields = [
            order.street,
            order.number,
            order.district,
            order.city,
            order.state,
            order.zip_code,
        ]
        return not any(field in [None, ''] for field in required_fields)

    def list(self, request):
        """
        Lista todos os pagamentos do usuário
        """
        payments = Payment.objects.filter(
            order__user=request.user
        ).order_by('-created_at')

        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Detalhe de um pagamento
        """
        payment = get_object_or_404(
            Payment,
            id=pk,
            order__user=request.user
        )

        serializer = PaymentSerializer(payment)
        return Response(serializer.data)


    @transaction.atomic
    def create(self, request):
        order_id = request.data.get('order')
        method = request.data.get('method')

        if not order_id or not method:
            return Response(
                {'detail': 'order and method are required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        order = get_object_or_404(
            Order,
            id=order_id,
            user=request.user
        )

        if order.status != 'pending':
            return Response(
                {'detail': 'Order cannot be paid'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # impede pagamento duplicado aprovado
        if order.payments.filter(status='approved').exists():
            return Response(
            {'detail': 'Order already has an approved payment'},
            status=status.HTTP_400_BAD_REQUEST
        )

        # validação do snapshot
        if not self._order_has_address_snapshot(order):
            return Response(
                {'detail': 'Order has no address snapshot. Checkout is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        payment = Payment.objects.create(
            order=order,
            method=method,
            amount=order.total_amount,
            status='pending'
        )

        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @transaction.atomic
    def approve(self, request, pk=None):
        payment = get_object_or_404(
            Payment,
            id=pk,
            order__user=request.user
        )

        if payment.status != 'pending':
            return Response(
                {'detail': 'Payment already processed'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        order = payment.order

        #   impede aprovação duplicada
        if order.payments.filter(status='approved').exclude(id=payment.id).exists():
            return Response(
                {'detail': 'Order already paid'},
                status=status.HTTP_400_BAD_REQUEST
        )

        # Validação do snapshot
        if not self._order_has_address_snapshot(order):
            return Response(
                {'detail': 'Order has no address snapshot. Checkout is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Simula resposta de gateway
        payment.status = 'approved'
        payment.transaction_id = str(uuid.uuid4())
        payment.save()

        order.status = 'paid'
        order.save()

        # Limpa o carrinho
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart.items.all().delete()

        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    @transaction.atomic
    def fail(self, request, pk=None):
        payment = get_object_or_404(
            Payment,
            id=pk,
            order__user=request.user
        )

        if payment.status != 'pending':
            return Response(
                {'detail': 'Payment already processed'},
                status=status.HTTP_400_BAD_REQUEST
            )

        payment.status = 'failed'
        payment.save()

        serializer = PaymentSerializer(payment)
        return Response(serializer.data)
