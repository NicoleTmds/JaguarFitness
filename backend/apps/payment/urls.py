from django.urls import path
from .views import PaymentViewSet

payment_list_create = PaymentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

payment_detail = PaymentViewSet.as_view({
    'get': 'retrieve'
})

payment_approve = PaymentViewSet.as_view({
    'post': 'approve'
})

payment_fail = PaymentViewSet.as_view({
    'post': 'fail'
})

urlpatterns = [
    path('', payment_list_create, name='payment-list-create'),
    path('<int:pk>/', payment_detail, name='payment-detail'),
    path('<int:pk>/approve/', payment_approve, name='payment-approve'),
    path('<int:pk>/fail/', payment_fail, name='payment-fail'),
]
