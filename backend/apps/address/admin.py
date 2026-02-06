from django.contrib import admin
from .models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'street',
        'number',
        'district',
        'city',
        'state',
        'zip_code',
    )

    list_filter = (
        'state',
        'city',
    )

    search_fields = (
        'street',
        'district',
        'city',
        'zip_code',
        'user__username',
        'user__email',
    )

    ordering = ('-id',)
