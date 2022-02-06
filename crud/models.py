from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),

)
# Create your models here.
class Product(models.Model):
     name= models.CharField(max_length= 100, null=True  )
     category=models.CharField(max_length=20, choices= CATEGORY)
     quantity=models.PositiveIntegerField(null=True)
     
     def __str__(self):
         return f'{self.name}'
     

class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE,)
    staff=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity= models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self) -> str:
        return f'{self.order_quantity}-->{self.product} placed by {self.staff.username} '


