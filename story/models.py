import os.path

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


