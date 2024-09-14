from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    price=models.FloatField()
    file=models.FileField(upload_to='uploads')
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    total_sales_amount=models.IntegerField(default=0)
    total_sales=models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.name
    
class OrderDetails(models.Model):
    customer_email=models.EmailField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    amount=models.IntegerField()
    stripe_payment_intent = models.CharField(max_length=255, blank=True, null=True)
    checkout_session_id = models.CharField(max_length=255, blank=True, null=True)  
    has_payed=models.BooleanField(default=False)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now_add=True)