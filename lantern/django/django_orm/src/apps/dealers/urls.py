
from django.urls import path

from apps.dealers.views import DealerListView, DealerInfoView, DealerCarListView

app_name = "dealers"

urlpatterns = [
    path("", DealerListView.as_view(), name="dealers"),
    path("<int:id>/", DealerCarListView.as_view(), name="dealer_car"),
]