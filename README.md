<h2 alingn='center'>Movie</h2>

### Описание проекта:
    Сайт для просмотра фильмов.
    Есть подписка на рассылку, и уведомляет о новых фильмов.

## Разработка



##### 1) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 2) Создать виртуальное окружение

    python -m venv venv
    
##### 3) Активировать виртуальное окружение

    venv\Scripts\activate.bat - Windows

    venv/bin/activate - Linux or Mac

##### 4) Устанавливить зависимости:

    pip install -r req.txt

##### 5) Выполнить команду для выполнения миграций

    python manage.py migrate
    
##### 6) Создать суперпользователя

    python manage.py createsuperuser
    
##### 7) Запустить сервер

    python manage.py runserver

##### 8) Запустить redis

    docker run -d -p 6379:6379 redis
    
##### 9) Запустить celery

    celery -A config worker -l info
