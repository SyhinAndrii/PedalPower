from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories', views.categories, name='categories'),
    path('products/<str:category_slug>', views.view_products, name='products'),

]