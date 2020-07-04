from apps.cars.models import Car
from apps.dealers.models import Dealer
from django.views.generic import DetailView, ListView


class DealerListView(ListView):
    model = Dealer
    template_name = "dealers.html"


class DealerInfoView(DetailView):
    model = Car
    context_object_name = "car"
    template_name = "dealer_car.html"
    pk_url_kwarg = "id"

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DealerCarListView(ListView):
    model = Car
    template_name = 'dealer_car.html'
    paginate_by = 10

    def get_queryset(self):
        query = Car.objects.all()
        dealer = self.kwargs.get('id')
        if dealer is not None:
            return query.filter(dealer=dealer)
        else:
            return query
