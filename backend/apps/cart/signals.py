from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from .services import merge_carts

@receiver(user_logged_in)
def merge_cart_on_login(sender, request, user, **kwargs):
    session_key = request.session.session_key
    if session_key:
        merge_carts(session_key, user)
