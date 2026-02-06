from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Authentication routes
    path('admin/', admin.site.urls),

    path('api/auth/', include('apps.accounts.urls')),

    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Cart flow
    path('api/cart/', include('apps.cart.urls')),

    # Order flow
    path('api/order/', include('apps.order.urls')),

    # Payment flow
    path('api/payment/', include('apps.payment.urls')),

    # Address flow
    path('api/address/', include('apps.address.urls')),
]
