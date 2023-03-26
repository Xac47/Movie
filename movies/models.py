from datetime import date

from django.db import models


class Category(models.Model):
    """ Категории """
    name = models.CharField('Категория', max_length=120)
    desc = models.TextField('Описание')
    url = models.SlugField(max_length=170, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Actor(models.Model):
    """ Актеры и режиссеры """
    name = models.CharField('Имя', max_length=100)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    desc = models.TextField('Описание')
    image = models.ImageField('Фото', upload_to='actors/')

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """ Жанры """
    name = models.CharField('Имя', max_length=100)
    desc = models.TextField('Описание')
    url = models.SlugField(max_length=170, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Movie(models.Model):
    """ Фильмы """
    title = models.CharField('Название', max_length=100)
    tagline = models.CharField('Слоган', max_length=100, default='')
    desc = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Дата выхода', default=2010)
    country = models.CharField('Страна', max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name='режиссер', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='актеры', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='жанры', related_name='film_genre')
    world_premiere = models.DateField('Примьера в мире', default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default=0, help_text='указывать сумму в долларах')
    fees_in_usa = models.PositiveIntegerField(
        'Сборы в США', default=0, help_text='указывать сумму в долларах'
    )
    fees_in_world = models.PositiveIntegerField(
        'Сборы в мире', default=0, help_text='указывать сумму в долларах'
    )
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('Черновик', default=False)
    comments_on_off = models.BooleanField('Комментарии вкл/выкл', default=True)
    create_at = models.DateTimeField('Обуликовано', auto_now_add=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title


class MovieShots(models.Model):
    """ Кадры из фильма """
    title = models.CharField('Заголовок', max_length=100)
    desc = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'

    def __str__(self):
        return self.title


class RatingStar(models.Model):
    """ Звезда рейтинга """
    value = models.SmallIntegerField('Значение', default=0)

    class Meta:
        verbose_name = 'Звезда рейтинг'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    """ Рейтинг """
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return f'{self.star} - {self.movie}'


class Review(models.Model):
    """ Отзывы """
    email = models.EmailField()
    name = models.CharField('Имя', max_length=20)
    text = models.TextField('Сообщение', max_length=5000)
    create_at = models.DateTimeField('Создан', auto_now_add=True)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.name} - {self.email}'