from apps.cars.views import CarViewSet, CarListView
from django.urls import path
from rest_framework import routers

from apps.cars.views import CarUpdDelView, CarCreateView

app_name = 'cars'

router = routers.SimpleRouter()
router.register(r'', CarViewSet)

urlpatterns = [

                  path('car/', CarListView.as_view(), name="car_of_dealers"),
                  path('car/created/', CarCreateView.as_view(), name='car_creation'),
                  path('car/<int:pk>/', CarUpdDelView.as_view(), name='car_upd_del')

              ] + router.urls
