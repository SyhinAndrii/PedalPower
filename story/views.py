from django.shortcuts import render
from .models import Category


# Create your views here.
def home(request):
    return render(request, "story/index.html")


def categories(request):
    cat = Category.get_categories()
    context = {'categories': cat}
    return render(request, "story/categories.html", context=context)
