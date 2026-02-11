from celery import shared_task
from django.utils import timezone

from atomic_habits.models import Habit


@shared_task
def send_user_message():
    """
    Отправка привычки пользователю
    """

    today = timezone.now().today().date()
    habits = Habit.objects.all()
    for habit in habits:
        if today == habit.time:
            print(habit)
            return str(habit)