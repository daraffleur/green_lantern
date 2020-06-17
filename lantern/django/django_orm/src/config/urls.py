
"""car_dealer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from apps.cars.views import CarListView, CarAdditionalInfoView
from apps.dealers.views import DealerListView, DealerCarListView
from apps.newsletters.views import NewsLetterView
from apps.orders.views import OrderView
from common.views import LoginView, logout_view, main_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_view, name="main_page"),
    # path("success/", TemplateView.as_view(template_name="index.html",), name="success"),
    path("", TemplateView.as_view(template_name="index.html", ), name="success"),
    path("newsletter/", NewsLetterView.as_view(), name="newsletter"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("cars/", CarListView.as_view(template_name="list_of_cars.html"), name='list_of_cars'),
    path("cars/<int:id>", CarAdditionalInfoView.as_view(template_name="car_additional_info.html"), name="info"),
    path("dealers/", DealerListView.as_view(template_name='dealers.html'), name='dealers'),
    path("dealers/<int:id>/", DealerCarListView.as_view(template_name='dealer_car.html'), name='dealer_car'),
    path("order/", OrderView.as_view(), name="order"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
