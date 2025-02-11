from django.db import models
from django.conf import settings


class Product(models.Model):
    name =models.CharField(max_length=225, null=True)
    description= models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock= models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
   
class CartItem(models.Model):
    cart=models.ForeignKey(Cart, related_name='items',on_delete=models.CASCADE)
    product =models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"



