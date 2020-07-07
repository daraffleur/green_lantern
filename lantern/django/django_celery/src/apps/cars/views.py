from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.cars.models import Car
from apps.cars.permissions import CarIsAuthenticatedOrPublicOnly
from apps.cars.serializers import CarSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (CarIsAuthenticatedOrPublicOnly,)

    # def get_queryset(self):
    #     return Car.objects.filter(dealer=self.request.user)

    @action(detail=False, methods=('get',))
    def public(self, request):
        queryset = self.filter_queryset(Car.objects.all())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


def view_cars(request, *args, **kwargs):
    try:
        num_car_views = Car.objects.get(slug=Car.slug)
    except Car.DoesNotExist:
        raise Http404("Car does not exist")

    num_car_views.views += 1
    num_car_views.save()
    return render(request, 'car_views.html', context={'car_views': num_car_views})


def cars_orders(request, *args, **kwargs):
    try:
        num_car_orders = Car.objects.get(slug=Car.slug)
    except Car.DoesNotExist:
        raise Http404("Car does not exist")

    num_car_orders.status += 1
    num_car_orders.save()

    return render(request, 'car_orders.html', context={'car_orders': num_car_orders})
