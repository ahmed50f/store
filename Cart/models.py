from django.db import models
from products.models import Product
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey('auth.User', related_name='cart', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart of {self.user.username}"
    
class CartItem(models.Model):    
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.title} in {self.cart.user.username}'s cart"