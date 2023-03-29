from django.shortcuts import render, redirect
from .models import Product, Cart


def cart_add(request, product_id):
    if request.user.is_authenticated:
        Cart.add_product_to_cart(request.user, product_id)
        return redirect('cart')
    else:
        print('Login to continue')
        return redirect('login')


def cart_view(request):
    if request.user.is_authenticated:
        cart_items = Cart.get_cart_products(request.user)

        context = {
            "cart_items": cart_items
        }
    else:
        print('Login to continue')
        return redirect('login')

    return render(request, "story/inc/card.html", context)
