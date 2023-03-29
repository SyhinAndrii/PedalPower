from django.contrib import admin

from story.models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Specifications)
admin.site.register(Cart)
