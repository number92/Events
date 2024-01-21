from datetime import date as d
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from drf_extra_fields.fields import Base64ImageField
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from events.models import Event
from organizations.models import Organization
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "phone_number",
            "username",
        )


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="Пользователь с таким email существует",
            )
        ],
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )
        extra_kwargs = {
            "password": {"write-only": True},
        }

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class CreateOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            "title",
            "description",
            "address",
            "postcode",
        )

        def validate(self, attrs):
            if not hasattr(attrs, "title"):
                raise ValidationError("Нужно указать Наименование")
            if not hasattr(attrs, "address"):
                raise ValidationError("Нужно указать Адрес")
            if not hasattr(attrs, "postcode"):
                raise ValidationError("Нужно указать Почтовый индекс")
            return attrs

        def create(self, validated_data):
            organization = Organization(**validated_data)
            return organization


class OrganizationWithMembersSerializer(serializers.ModelSerializer):
    full_address = serializers.SerializerMethodField()

    members = UserSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Organization
        fields = (
            "title",
            "description",
            "full_address",
            "members",
        )

    def get_full_address(self, obj):
        postcode = obj.postcode
        address = obj.address
        return f"{postcode}, {address}."


class CreateEventSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    date = serializers.DateField()

    class Meta:
        model = Event
        fields = (
            "title",
            "description",
            "date",
            "image",
        )
        extra_kwargs = {"description": {"required": False}}

    def validate(self, attrs):
        today = d.today()
        if attrs["date"] < today:
            raise ValidationError(f"Дата не может быть ранее {today}")
        return attrs

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)
        return event


class GetEventSerializer(serializers.ModelSerializer):
    organizations = OrganizationWithMembersSerializer(
        read_only=True, many=True
    )
    image = Base64ImageField(required=False)

    class Meta:
        model = Event
        fields = (
            "title",
            "description",
            "date",
            "image",
            "organizations",
        )
