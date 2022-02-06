from django.shortcuts import render
from crud.serializers import OrderSerializer, ProductSerializer
from rest_framework import viewsets
from .models import Product, Order

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset= Order.objects.all()
    serializer_class= OrderSerializer    
    
    
