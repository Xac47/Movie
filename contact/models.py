from django.db import models

class SubscribeEmail(models.Model):
    email = models.EmailField(max_length=90)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'E-mail'
        verbose_name_plural = 'E-mails'

    def __str__(self):
        return f'{self.email} - {self.create_at}'

