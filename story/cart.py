from django.shortcuts import render, redirect
from .models import Product, Cart
from django.contrib import messages


def cart_add(request, product_id):
    if request.user.is_authenticated:
        product_count = 1
        if request.POST:
            product_count = int(request.POST['quantity'])
        Cart.add_product_to_cart(request.user, product_id, product_count)

        messages.success(request, f'Added to cart successfully')
        return redirect(request.META.get('HTTP_REFERER'))

    else:
        print('Login to continue')
        return redirect('login')


def cart_remove(request, product_id):
    cart_id = Cart.objects.get(user_id=request.user)
    Cart.remove_item(product_id, cart_id)
    return redirect("cart")


def cart_view(request):
    if request.user.is_authenticated:
        cart_items = Cart.get_cart_items(request.user)
        context = {
            "cart_items": cart_items,
            'total_price': Cart.get_total_price(cart_items)
        }
    else:
        print('Login to continue')
        return redirect('login')

    return render(request, "story/inc/card.html", context=context)
