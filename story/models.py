import os.path

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


def get_category_path(instance, filename):
    now_time = datetime.now().strftime("%d_%m_%Y_%H:%M:%S ")
    filename = now_time + filename
    return os.path.join("uploads/category/", filename)


def get_product_path(instance, filename):
    now_time = datetime.now().strftime("%d_%m_%Y_%H:%M:%S ")
    filename = now_time + instance.name
    return os.path.join(f"uploads/products/{instance.category.slug}/", filename)


class Category(models.Model):
    slug = models.CharField(max_length=100, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to=get_category_path, null=True, blank=True)
    description = models.TextField(max_length=500, blank=False, null=False, default="")
    trending = models.BooleanField(default=False, help_text="0-default, 1-Trending")
    status = models.BooleanField(default=False, help_text="0-default, 1-Hidden")

    def __str__(self):
        return self.name

    @classmethod
    def get_categories(cls):
        return cls.objects.filter(status=0)


class Brand(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=False)

    def __str__(self):
        return self.name


class Specifications(models.Model):
    MATERIAL_CHOICES = [
        ('Алюміній', 'Алюміній'),
        ('Карбон', 'Карбон'),
        ('Сталь', 'Сталь'),
        ('Хром-Молібден (CrMo)', 'Хром-Молібден (CrMo)')
    ]
    BRAKES_CHOICE = [
        ('Дискові механічні', 'Дискові механічні'),
        ('Дискові гідравлічні', 'Дискові гідравлічні'),
        ('Ободні V-brake', 'Ободні V-brake')
    ]
    material = models.CharField(max_length=50, blank=False, null=False, choices=MATERIAL_CHOICES)
    wheel_diameter = models.FloatField(blank=True, null=True)
    frame_size = models.CharField(max_length=64, blank=True, null=False)
    type_of_brakes = models.CharField(max_length=64, blank=True, null=False)
    amount_of_speeds = models.IntegerField(blank=True, null=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)
    product_image = models.ImageField(upload_to=get_product_path, null=True, blank=True)
    description = models.TextField(max_length=500, blank=False, null=False)
    original_price = models.FloatField(blank=False, null=False)
    selling_price = models.FloatField(blank=False, null=False)
    trending = models.BooleanField(default=False, help_text="0-defauld, 1-Trending")
    status = models.BooleanField(default=False, help_text="0-default, 1-Hidden")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    specifications = models.OneToOneField(Specifications, on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True, help_text="is the product in stock")

    def __str__(self):
        return self.name

    @classmethod
    def get_products_by_category(cls, category_slug):
        if Category.objects.filter(slug=category_slug, status=0):
            data = cls.objects.filter(category__slug=category_slug)
            category = Category.objects.filter(slug=category_slug).first()
            return data, category
        return None, None

    @classmethod
    def get_product_by_id(cls, product_id):
        product = cls.objects.get(pk=product_id, status=0)
        return product

    @classmethod
    def get_top_products(cls):
        products = cls.objects.filter(trending=True)
        return products


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through="CartItem")

    @classmethod
    def add_product_to_cart(cls, user, product_id, product_count):
        product = Product.get_product_by_id(product_id)
        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity = product_count
        cart_item.save()

    @classmethod
    def remove_item(cls, product_id, cart):
        CartItem.objects.get(product_id=product_id, cart=cart).delete()

    @classmethod
    def get_cart_items(cls, user):
        user_cart, created = Cart.objects.get_or_create(user=user)
        cart_items = user_cart.cartitem_set.all()

        return cart_items

    @classmethod
    def get_total_price(cls, cart_items):
        price = []
        for item in cart_items:
            price.append(item.product.selling_price * item.quantity)
        return sum(price)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
        ('REFUNDED', 'Refunded'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Order {self.id} ({self.user.username})'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.price * self.quantity
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.product_name} ({self.quantity})'






