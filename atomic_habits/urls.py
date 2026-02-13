from django.urls import path

from atomic_habits.apps import AtomicHabitsConfig
from atomic_habits.views import (HabitCreateAPIView, HabitDestroyAPIView, HabitListAPIView, HabitRetrieveAPIView,
                                 HabitUpdateAPIView)

app_name = AtomicHabitsConfig.name

urlpatterns = [
    # привычки
    path("habits/", HabitListAPIView.as_view(), name="habits_list"),
    path("public_habits/", HabitPublicListAPIView.as_view(), name="public_habits_list"),
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habits_retrieve"),
    path("habits/create/", HabitCreateAPIView.as_view(), name="habits_create"),
    path(
        "habits/<int:pk>/delete/",
        HabitDestroyAPIView.as_view(),
        name="habits_delete",
    ),
    path("habits/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habits_update"),
]
