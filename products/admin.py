from django.contrib import admin
from .models import Category, Product, Rating , Order, Shipping


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity', 'available', 'category')
    search_fields = ('title', 'category__name')
    list_filter = ('available', 'category')     

class RatingAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating', 'comment')
    search_fields = ('product__title',)
    list_filter = ('rating',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'order_date')
    search_fields = ('product__title',)
    list_filter = ('order_date',)

class ShippingAdmin(admin.ModelAdmin):
    list_display = ('product', 'shipping_date_display', 'quantity')

    def shipping_date_display(self, obj):
        return obj.delivery_date
    shipping_date_display.short_description = 'Estimated Delivery Date'




admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Shipping, ShippingAdmin)
