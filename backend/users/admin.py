from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Пользователи"""

    list_display = (
        "id",
        "username",
        "email",
        "is_active",
        "phone_number",
    )
    save_on_top = True

    list_editable = ("is_active",)
    list_filter = ("is_active",)
    search_fields = (
        "id",
        "email",
        "phone_number",
    )
