from apps.cars.models import Car
from apps.cars.permissions import CarIsAuthenticatedOrPublicOnly
from apps.cars.serializers import CarSerializer
from apps.dealers.models import Dealer
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (CarIsAuthenticatedOrPublicOnly,)

    @action(detail=False, methods=('get',))
    def public(self, request):
        queryset = self.filter_queryset(Car.objects.all())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_queryset(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Car.objects.filter(dealer=self.request.user.id)


class CarGenericAPIView(CreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def perform_create(self, serializer):
        serializer.save(dealer=self.request.username)


class CarCreateView(ListCreateAPIView, CarListView):

    def perform_create(self, serializer):
        return serializer.save(dealer=get_object_or_404(Dealer, id=self.request.data.get('dealer')))


class CarUpdDelView(RetrieveUpdateDestroyAPIView, CarListView):

    def retrieve(self, request, *args, **kwargs):
        user = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        return Response(self.serializer_class(user).data)
