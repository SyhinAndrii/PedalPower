import os.path

from django.db import models
from datetime import datetime


def get_category_path(instance, filename):
    now_time = datetime.now().strftime("%d_%m_%Y %H:%M:%S ")
    filename = now_time + filename
    return os.path.join(f"uploads/category/", filename)


def get_product_path(instance, filename):
    now_time = datetime.now().strftime("%d_%m_%Y %H:%M:%S ")
    filename = now_time + filename
    return os.path.join(f"uploads/products/{instance.category.name}/", filename)


class Category(models.Model):
    slug = models.CharField(max_length=100, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to=get_category_path, null=True, blank=True)
    description = models.TextField(max_length=500, blank=False, null=False, default="")
    trending = models.BooleanField(default=False, help_text="0-default, 1-Trending")
    status = models.BooleanField(default=False, help_text="0-default, 1-Hidden")

    def __str__(self):
        return self.name


class Brand(models.Model):
    pass


class Specifications(models.Model):
    pass


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
    specifications = models.ForeignKey(Specifications, on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True, help_text="is the product in stock")
