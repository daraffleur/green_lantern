from apps.cars.models import Car
from apps.photos.forms import UploadPhotoForm
from apps.photos.models import Photo
from django.urls import reverse_lazy
from django.views.generic import FormView


class UploadPhotoView(FormView):
    template_name = 'images.html'
    model = Photo

    form_class = UploadPhotoForm
    success_url = reverse_lazy("list_of_cars")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_queryset(self):
        query = Car.objects.all()
        dealer = self.kwargs.get('id')
        list_of_cars = query.filter(username=dealer).values_list('cars', flat=True)
        return query.filter(id__in=list_of_cars)
