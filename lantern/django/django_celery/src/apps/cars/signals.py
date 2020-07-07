from datetime import datetime

from django.db import models
from django.dispatch import receiver

from apps.cars.models import Car
from apps.cars.tasks import send_notification, publish_at


@receiver(models.signals.post_save, sender=Car)
def notify_by_emails(sender, instance, **kwargs):
    if instance.status == Car.STATUS_PUBLISHED:
        send_notification.delay(instance.pk)


@receiver(models.signals.post_save, sender=Car)
def notify_about_publishing(sender, instance, **kwargs):
    if instance.status == Car.STATUS_WAITING_FOR_PUBLISH:
        publish_at.apply_async(args=instance.pk, eta=datetime.now())
