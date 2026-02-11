from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # apps
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
]
