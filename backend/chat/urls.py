from django.urls import path

from . import views


urlpatterns = [
    path("ws/", views.index, name="index"),
    path("ws/<str:room_name>/", views.room, name="room"),
]