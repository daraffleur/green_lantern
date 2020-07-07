from django.core.mail import send_mail
from django.template import Template, Context
from apps.cars.models import Car
from apps.newsletters.models import NewsLetter
from common.celery import app

REPORT_TEMPLATE_VIEWS = """
{% for car_view in car_views %}
        "{{ car.model }}": viewed {{ car.views }} times |
{% endfor %}
"""

REPORT_TEMPLATE_ORDERS = """
{% for car_order in car_orders %}
        "{{ car.model }}" was in status 'pending' {{ car.status }} times |
{% endfor %}
"""

@app.task()
def send_view_count_report():
    for user in Car.objects.filter(user=Car.dealer):
        car_views = Car.objects.filter(author=user)
        if not car_views:
            continue
        template = Template(REPORT_TEMPLATE_VIEWS)
        send_mail(
            'Views Activity',
            template.render(context=Context({'car_views': car_views})),
            'from@quickpublisher.dev',
            [user.email],
            fail_silently=False,
        )

@app.task()
def send_order_count_report():
    status = Car.objects.filter(status=Car.status)
    for user in Car.objects.filter(user=Car.dealer):
        car_orders = Car.objects.filter(author=user, status=status)
        if not car_orders:
            continue

        template = Template(REPORT_TEMPLATE_ORDERS)

        send_mail(
            'Orders Activity',
            template.render(context=Context({'car_views': car_orders})),
            'from@quickpublisher.dev',
            [user.email],
            fail_silently=False,
        )

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
