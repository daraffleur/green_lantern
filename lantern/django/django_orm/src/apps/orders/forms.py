
from django.forms import models

from apps.orders.models import Order


class OrderModelForm(models.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
