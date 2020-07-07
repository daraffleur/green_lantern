from django.core.mail import send_mail

from apps.newsletters.models import NewsLetter
from common.celery import app


@app.task()
def publish_at(car_id: int):
    from apps.cars.models import Car
    from datetime import datetime

    Car.objects.filter(id=car_id,
                       date_published__lte=datetime.now(),
                       status=Car.STATUS_WAITING_FOR_PUBLISH
                       ).update(status=Car.STATUS_WAITING_FOR_PUBLISH)


@app.task()
def send_notification(car_id: int):
    from apps.cars.models import Car

    car = Car.objects.filter(id=car_id, status=Car.STATUS_PUBLISHED)

    emails = NewsLetter.objects.all().values_list('email', flat=True)

    print('Working...')

    send_mail(subject=f'New car: {car}',
              message='Hi, ...',
              recipient_list=emails,
              from_email='settings.from_mail@gmail.com')
