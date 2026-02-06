from django.urls import path
from .views import OrderViewSet

order_list = OrderViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

order_detail = OrderViewSet.as_view({
    'get': 'retrieve',
})

order_cancel = OrderViewSet.as_view({
    'post': 'cancel',
})

urlpatterns = [
    path('', order_list, name='order-list-create'),
    path('<int:pk>/', order_detail, name='order-detail'),
    path('<int:pk>/cancel/', order_cancel, name='order-cancel'),
]
