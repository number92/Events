from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("chat/", include("chat.urls")),
    path("api/", include("api_v1.urls")),
    path("admin/", admin.site.urls),
]
