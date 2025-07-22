from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta
from django.utils.timezone import now

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
class Rating(models.Model):
    product = models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey('auth.User', related_name='ratings', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.title} - {self.rating}"
    
class Order(models.Model):
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.product.title} - {self.quantity} pcs"
    
class Shipping(models.Model):
    product = models.ForeignKey(Product, related_name='shipping', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    address = models.CharField(max_length=255, default="Default Address")
    city = models.CharField(max_length=100, default="Default City")
    state = models.CharField(max_length=100, default="Default State")
    zip_code = models.CharField(max_length=20, default="Default Zip Code")
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def delivery_date(self):
        min_day =2
        max_day = 5
        avg_day = (min_day + max_day) // 2
        return self.created_at + timedelta(days=avg_day)
    
    def __str__(self):
        return f"Shipping for {self.product.name} - Quantity: {self.quantity}"
