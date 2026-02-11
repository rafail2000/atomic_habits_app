from rest_framework import serializers

from atomic_habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели привычки
    """

    class Meta:
        model = Habit
        fields = "__all__"
