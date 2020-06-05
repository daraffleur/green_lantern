from django.db import models
from django.db.models import Index
from django.utils.translation import gettext_lazy as _

from common.models import BaseDateAuditModel


class Order(BaseDateAuditModel):
    STATUS_EXPECTED = 'expected'
    STATUS_VERIFIED = 'verified'
    STATUS_PAID_OUT = 'paid_out'

    STATUS_CHOICES = (
        (STATUS_EXPECTED, "Expected"),
        (STATUS_VERIFIED, "Verified"),
        (STATUS_PAID_OUT, "Paid_out"),
    )

    order_id = models.AutoField(primary_key=True)
    car_id = models.ForeignKey(to='Car', db_column='car', blank=True, null=False, on_delete=models.DO_NOTHING,
                               db_constraint=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_EXPECTED, blank=True)
    first_name = models.CharField(max_length=30, blank=True, null=False)
    last_name = models.CharField(max_length=30, blank=True, null=False)
    email = models.EmailField(max_length=70, blank=True, null=False, unique=True)
    phone = models.CharField(max_length=50, blank=True, null=False, unique=True)
    message = models.CharField(max_length=32, blank=True, null=False)
    views = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

        indexes = [
            Index(fields=['status', ])
        ]
