import json

from django.shortcuts import render, redirect
from .models import Category, Product, Cart


# Create your views here.
def home(request):
    top_bicycle = Product.get_top_products()
    context = {
        'products': top_bicycle,
    }
    return render(request, "story/index.html", context)


def categories(request):
    category = Category.get_categories()
    context = {'categories': category}
    return render(request, "story/categories.html", context=context)


def view_products(request, category_slug):
    products, category = Product.get_products_by_category(category_slug)
    if products:
        context = {
            'products': products,
            'category': category, }
        return render(request, "story/products/index.html", context=context)

    return redirect("categories")


def product_details_view(request, category_slug, product_id):
    product = Product.get_product_by_id(product_id)
    if product:
        context = {
            'product': product
        }
        return render(request, "story/products/product_page.html", context=context)
    return redirect(request, 'categories')


def payment(request):
    cart_items = Cart.get_cart_items(request.user)
    context = {
        "cart_items": cart_items,
        'total_price': Cart.get_total_price(cart_items)
    }
    return render(request, "story/inc/payment.html", context)














