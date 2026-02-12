# Atomic habits app.

SPA веб-приложение для трекинга полезных привычек,
данная задумка вдохновлено книгой «Атомные привычки»
Джеймса Клира.

Для запуска приложения нужно выполнить следующие предписания:
1) Активировать виртуальное окружение
2) создать и заполнить .env файл
3) запустить сервер redis
4) Выполнить команды в терминале:

    poetry install
    python manage.py migrate
    python manage.py csu
    python manage.py runserver
    celery -A config worker --pool=solo --loglevel=info
    celery -A config beat --loglevel=info

