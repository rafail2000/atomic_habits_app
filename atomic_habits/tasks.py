from celery import shared_task
from django.utils import timezone

from atomic_habits.models import Habit


@shared_task
def send_user_message():
    """
    Отправка привычки пользователю
    """

    current_time = timezone.now().time()
    habits = Habit.objects.all()
    for habit in habits:
        if (habit.time and
            habit.time.hour == current_time.hour and
            habit.time.minute == current_time.minute):
            print(str(habit))
            return str(habit)