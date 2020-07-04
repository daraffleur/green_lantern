from apps.cars.models import Car
from django.views.generic import ListView, DetailView


class CarListView(ListView):
    template_name = "list_of_cars.html"
    model = Car
    paginate_by = 10


class CarAdditionalInfoView(DetailView):
    template_name = "car_additional_info.html"
    model = Car
    context_object_name = "car"
    pk_url_kwarg = "id"

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
