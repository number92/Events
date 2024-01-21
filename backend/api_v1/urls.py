from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegistrationView, CreateOrganizationView, EventsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    r"organizations", CreateOrganizationView, basename="organizations"
)
router.register(r"events", EventsView, basename="events")


urlpatterns = [
    path("", include(router.urls)),
    path("auth/signup/", RegistrationView.as_view(), name="signup"),
    path(
        "auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
