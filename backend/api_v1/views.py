from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework import generics, status, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from api_v1.utils import one_minute_sleep
from events.models import Event
from organizations.models import Organization
from api_v1.serializers import (
    CreateEventSerializer,
    GetEventSerializer,
    RegistrationSerializer,
    CreateOrganizationSerializer,
)


class RegistrationView(generics.CreateAPIView):
    """Представление регистрации"""

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CreateOrganizationView(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """Создание организации"""

    queryset = Organization.objects.all()
    serializer_class = CreateOrganizationSerializer
    permission_classes = (IsAuthenticated,)


class EventsView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """Представление Мероприятия. Методы: retrieve, list, post"""

    queryset = Event.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_fields = ("date",)
    search_fields = ("title",)
    ordering_fields = ("date",)
    ordering = ("date",)

    def get_serializer_class(self):
        if self.action in ("create", "post"):
            return CreateEventSerializer
        return GetEventSerializer

    def get_queryset(self):
        if self.action in ("create", "post"):
            return Event.objects.all()
        queryset = Event.objects.prefetch_related("organizations")
        return queryset

    async def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
        )
        if serializer.is_valid(raise_exception=True):
            await one_minute_sleep()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
