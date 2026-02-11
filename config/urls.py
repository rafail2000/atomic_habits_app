from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # apps
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("atomic_habits/", include("atomic_habits.urls", namespace="atomic_habits")),
]
