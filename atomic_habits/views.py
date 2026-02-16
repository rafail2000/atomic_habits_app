from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from atomic_habits.models import Habit
from atomic_habits.paginations import CustomPagination
from atomic_habits.serializers import HabitSerializer
from users.permissions import IsModerator, IsOwner


class HabitCreateAPIView(CreateAPIView):
    """
    Курсор для создания привычек
    """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitListAPIView(ListAPIView):
    """
    Курсор для просмотра списка привычек
    """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(ListAPIView):
    """
    Курсор для просмотра списка привычек
    """

    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)


class HabitRetrieveAPIView(RetrieveAPIView):
    """
    Курсор для просмотра привычки
    """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (
        IsAuthenticated,
        IsModerator | IsOwner,
    )


class HabitUpdateAPIView(UpdateAPIView):
    """
    Курсор для обновления привычки
    """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (
        IsAuthenticated,
        IsModerator | IsOwner,
    )


class HabitDestroyAPIView(DestroyAPIView):
    """
    Курсор для удаления привычки
    """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner | ~IsModerator)
