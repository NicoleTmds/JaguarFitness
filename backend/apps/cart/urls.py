from django.urls import path
from .views import CartViewSet

cart = CartViewSet.as_view({
    'get': 'retrieve'
})

add_item = CartViewSet.as_view({
    'post': 'add_item'
})

urlpatterns = [
    path('', cart, name='cart-detail'),
    path('add/', add_item, name='cart-add'),
]
