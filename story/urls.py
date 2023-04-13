from django.urls import path
from . import views, cart

urlpatterns = [
    path('', views.home, name='home'),
    path('categories', views.categories, name='categories'),
    path('categories/<str:category_slug>', views.view_products, name='products'),
    path('categories/<str:category_slug>/<int:product_id>', views.product_details_view, name='product view'),
    path('add_to_cart/<int:product_id>', cart.cart_add, name='add to cart'),
    path('cart/', cart.cart_view, name='cart'),
    path('cart/remove/<int:product_id>', cart.cart_remove, name='cart remove'),
    path('cart/payment', views.payment, name='payment'),
    path('placeorder', views.create_order, name='placeorder'),
    path('feedback/', views.feedback, name='feedback'),


]