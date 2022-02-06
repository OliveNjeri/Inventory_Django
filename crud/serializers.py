from rest_framework import serializers
from .models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= ('id', 'name' , 'category', 'quantity')
        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields=('product', 'staff', 'order_quantity', 'date')        
        

                        