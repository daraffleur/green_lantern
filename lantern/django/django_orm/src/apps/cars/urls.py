
from django.urls import path

from apps.cars.views import CarListView, CarAdditionalInfoView

app_name = 'list_of_cars'

urlpatterns = [
    path("", CarListView.as_view(), name="list_of_cars"),
    path("cars/<int:id>/", CarAdditionalInfoView.as_view(), name="info"),

]
