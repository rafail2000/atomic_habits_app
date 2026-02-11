from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Habit(models.Model):
    """
    Модель привычки
    """

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Пользователь",
        help_text="Введите имя пользователя",
    )
    place = models.CharField(max_length=255, verbose_name="Место", help_text="Введите место")
    time = models.DateTimeField(
        verbose_name="Время для выполнения привычки", help_text="Введите время для выполнения привычки"
    )
    action = models.CharField(max_length=255, verbose_name="Действие", help_text="Введите действие")
    is_pleasant_habit = models.BooleanField(
        default=False, verbose_name="Приятной привычки", help_text="Укажите флаг приятной привычки"
    )
    related_habit = models.ForeignKey(
        "atomic_habits.Habit",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычку если она имеется",
    )
    periodicity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(7)],
        default=1,
        verbose_name="Периодичность",
        help_text="Укажите периодичность выполнения",
    )
    award = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Вознаграждение", help_text="Введите вознаграждение"
    )
    time_to_complete = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(120)],
        verbose_name="Время выполнения",
        help_text="Укажите выполнения выполнения",
    )
    is_public = models.BooleanField(default=False, verbose_name="Публикация", help_text="Укажите флаг публикации")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ["time"]

    def __str__(self):
        return f"я буду {self.action} в {self.time} в {self.place}"

    def clean(self):
        """
        Кастомная валидация данных для привычки
        """

        if self.related_habit and self.is_pleasant_habit:
            raise ValidationError("Нельзя указать одновременно связанную привычку и приятную привычку")

        if self.related_habit and not self.related_habit.is_pleasant_habit:
            raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки")

        if self.is_pleasant_habit and self.award or self.related_habit:
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")
