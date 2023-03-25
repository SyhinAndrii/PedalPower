from django.shortcuts import render
from .models import Category, Product


# Create your views here.
def home(request):
    return render(request, "story/index.html")


def categories(request):
    category = Category.get_categories()
    context = {'categories': category}
    return render(request, "story/categories.html", context=context)


def view_products(request, category_slug):
    data = Product.objects.filter(category__slug=category_slug)
    context = {'product_id': category_slug,
               'products': data,
               }
    return render(request, "story/products/index.html", context=context)
