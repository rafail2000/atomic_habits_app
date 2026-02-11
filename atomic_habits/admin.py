from django.contrib import admin

from atomic_habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_filter = (
        "id",
        "user",
        "place",
        "time",
        "action",
        "is_pleasant_habit",
        "related_habit",
        "periodicity",
        "award",
        "time_to_complete",
        "is_public",
    )
