from django.conf import settings
from django.core.mail import send_mail

from config.celery import app


@app.task()
def send_message_to_email_about_subscribe(user_email):
    send_mail(
        "Вы подписались на рассылку",
        'Мы будем вас оповещать об новых фильмов',
        f'{settings.EMAIL_HOST_USER}',
        [user_email],
        fail_silently=False
    )
