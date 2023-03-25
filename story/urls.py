from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories', views.categories, name='categories'),
    path('categories/<str:category_slug>', views.view_products, name='products'),
    path('categories/<str:category_slug>/<int:product_id>', views.product_details_view, name='product view'),
    path('test', views.test, name='test'),

]