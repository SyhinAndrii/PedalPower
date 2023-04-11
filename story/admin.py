from django.contrib import admin

from story.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'original_price', 'trending', 'brand')


class SpecificationsAdmin(admin.ModelAdmin):
    list_display = ('material', 'wheel_diameter', 'frame_size', 'type_of_brakes', 'amount_of_speeds')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Specifications, SpecificationsAdmin)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
