from django.db import models


class SubscribeEmail(models.Model):
    email = models.EmailField(max_length=90)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'E-mail'
        verbose_name_plural = 'E-mails'

    def __str__(self):
        return f'{self.email} - {self.create_at}'


class Contact(models.Model):
    title = models.CharField('Заголовок', max_length=30)
    desc = models.CharField('Описание', max_length=255)
    email = models.EmailField(unique=True)
    location = models.CharField('Локация', max_length=30)

    google_plus = models.URLField()
    twitter = models.URLField()
    facebook = models.URLField()
    dribbble = models.URLField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.title
