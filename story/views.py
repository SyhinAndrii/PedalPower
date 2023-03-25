from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Category, Product


# Create your views here.
def home(request):
    return render(request, "story/index.html")


def categories(request):
    category = Category.get_categories()
    context = {'categories': category}
    return render(request, "story/categories.html", context=context)


def view_products(request, category_slug):
    data, category = Product.get_products_by_category(category_slug)
    if data:
        context = {
            'products': data,
            'category': category, }
        return render(request, "story/products/index.html", context=context)

    messages.warning(request, 'Категорію не знайдено')
    return redirect("categories")


def product_details_view(request, category_slug, product_id):
    context = {
        'product': Product.get_product_by_id(product_id)
    }
    return render(request, "story/products/product_page.html", context=context)


def test(request):
    return render(request, "story/products/test.html")
