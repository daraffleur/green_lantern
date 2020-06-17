
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.orders.forms import OrderModelForm
from apps.orders.models import Order


class OrderView(FormView):
    template_name = "orders.html"
    model = Order

    form_class = OrderModelForm
    success_url = reverse_lazy("success")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def order_add(request):
        return render(request, 'orders/orders.html', {})
