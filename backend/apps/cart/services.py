from .models import Cart, CartItem

def merge_carts(session_key, user):
    try:
        session_cart = Cart.objects.get(session_key=session_key)
    except Cart.DoesNotExist:
        return

    user_cart, _ = Cart.objects.get_or_create(user=user)

    for item in session_cart.items.all():
        user_item, created = CartItem.objects.get_or_create(
            cart=user_cart,
            product=item.product,
            defaults={'quantity': item.quantity}
        )

        if not created:
            user_item.quantity += item.quantity
            user_item.save()

    session_cart.delete()
