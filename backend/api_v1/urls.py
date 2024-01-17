from django.urls import path, include


urlpatterns = [
    path(r"", include("djoser.urls")),
    path(r"auth/", include("djoser.urls.jwt")),
]
