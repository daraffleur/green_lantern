from django.db import models
from django.db.models import Index
from django.utils.translation import gettext_lazy as _

from apps.cars.managers import CarManager, CarQuerySet
from common.models import BaseDateAuditModel


class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        indexes = [
            Index(fields=('name',))
        ]

        verbose_name = _('Color')
        verbose_name_plural = _('Colors')

    def __str__(self):
        return self.name


class CarBrand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    logo = models.ImageField(null=True, blank=False)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',))
        ]
        verbose_name = _('Car brand')
        verbose_name_plural = _('Car brands')

    def __str__(self):
        return self.name


class CarModel(models.Model):
    model_id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ('name',)
        indexes = [
            Index(fields=('name',)),
        ]
        verbose_name = _('Car model')
        verbose_name_plural = _('Car models')

    def __str__(self):
        return self.name


class Car(BaseDateAuditModel):
    STATUS_PENDING = 'pending'
    STATUS_PUBLISHED = 'published'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived"),
    )
    car_id = models.AutoField(primary_key=True)
    color_id = models.ForeignKey(to='Color', on_delete=models.SET_NULL, null=True, blank=False, related_name='colour')
    dealer = models.ForeignKey(to='dealers.Dealer', on_delete=models.SET_NULL, null=True, blank=False, related_name='dealer')
    model_id = models.ForeignKey(to='CarModel', on_delete=models.SET_NULL, null=True, blank=False, related_name='model')
    engine_type = models.CharField(max_length=20)
    population_type = models.CharField(max_length=20)
    price = models.FloatField(blank=True, null=False)
    fuel_type = models.CharField(max_length=20)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_PENDING, blank=True)
    doors = models.ImageField(blank=True, null=False)
    capacity = models.FloatField(blank=True, null=False)
    gear_case = models.CharField(max_length=20, blank=True, null=False)
    number = models.FloatField(blank=True, null=False)
    slug = models.SlugField(max_length=75)
    sitting_place = models.ImageField(blank=True, null=False)
    first_registration_date = models.DateTimeField(auto_now=True)
    engine_power = models.FloatField(blank=True, null=False)

    objects = CarManager.from_queryset(CarQuerySet)()
    views = models.PositiveIntegerField(default=0, editable=False)
    number = models.CharField(max_length=16, unique=True)
    extra_title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Title second part'))

    # other fields ...
    #

    def save(self, *args, **kwargs):
        order_number_start = 7600000
        if not self.pk:
            super().save(*args, **kwargs)
            self.number = f"LK{order_number_start + self.pk}"
            self.save()
        else:
            super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.status = self.STATUS_ARCHIVED
        self.save()

    @property
    def title(self):
        return f'{self.model.brand} {self.extra_title or ""}'  # do not show None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')

        indexes = [
            Index(fields=['status', ])
        ]
