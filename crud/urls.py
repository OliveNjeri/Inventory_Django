from django.urls import path
from crud.views import ProductViewSet
from rest_framework import routers
from django.conf.urls import include
from .views import OrderViewSet, ProductViewSet

router= routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]