from django.urls import path
from rest_framework import routers

from apps.cars.views import CarViewSet, view_cars, cars_orders

app_name = 'cars'

router = routers.SimpleRouter()
router.register(r'', CarViewSet)

urlpatterns = [
    path('views/', view_cars, name='view_cars'),
    path('orders/', cars_orders, name='cars_orders'),

] + router.urls
