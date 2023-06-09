from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Category, Product, Cart, Order, CartItem, OrderItem, Feedback
from django.contrib import messages


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
            'category': category,
        }
        return render(request, "story/products/index.html", context=context)

    return redirect("categories")


def product_details_view(request, category_slug, product_id):
    product = Product.get_product_by_id(product_id)
    product_feedbacks = Feedback.get_feedbacks_by_product(product)

    # calculate average product rating
    rating = Feedback.average_product_rating(product_feedbacks)

    if product:
        context = {
            'product': product,
            'feedbacks': product_feedbacks,
            'rating': rating
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


def create_order(request):
    if request.method == 'POST':

        order = Order()
        order.user = request.user

        # Add products from the cart to the OrderItem model
        cart_items = CartItem.objects.filter(cart__user=request.user)
        total_price = Cart.get_total_price(cart_items)
        order.total_price = total_price
        order.save()
        for cart_item in cart_items:
            order_item = OrderItem()
            order_item.order = order
            order_item.product = cart_item.product
            order_item.quantity = cart_item.quantity
            order_item.price = cart_item.product.selling_price * cart_item.quantity
            order_item.save()

        # Redirect to the order detail page
        messages.success(request, 'Your order has been accepted successfully')
        return redirect('home')


def feedback(request):
    if request.user.is_authenticated:

        # get data from ajax
        rating = request.POST.get("rating")
        feedback_text = request.POST.get("feedback_text")

        # create new Feedback object
        feedback_obj = Feedback()
        feedback_obj.user = request.user
        feedback_obj.rate = rating
        feedback_obj.description = feedback_text
        feedback_obj.save()
        product = Product.get_product_by_id(request.POST.get('product_id'))
        feedback_obj.product.add(product)
        product.rating = Feedback.average_product_rating(Feedback.get_feedbacks_by_product(product))
        product.save()
        messages.success(request, "Feedback sent successfully")
        print(request.POST)
        return JsonResponse({
            "rating": rating,
            "feedback_text": feedback_text,
            "success": True
        })
    else:
        return JsonResponse({
            "success": False
        })
