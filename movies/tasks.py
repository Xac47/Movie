from django.conf import settings
from django.core.mail import send_mail

from config.celery import app
from contact.models import SubscribeEmail


@app.task()
def send_new_movie_notification_to_email(movie_name):
    for contact in SubscribeEmail.objects.all():
        send_mail(
            "Movie",
            f'Доступен новый фильм {movie_name}',
            f'{settings.EMAIL_HOST_USER}',
            [contact.email],
            fail_silently=False
        )
