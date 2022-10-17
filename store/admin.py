from django.contrib import admin
from .models import Product, UserOrder  # ProductImage
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'PRDName', 'PRDQuantity', 'PRDPrice',
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(UserOrder)
admin.site.site_header = "Shopping Store"
