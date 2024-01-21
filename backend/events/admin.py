from django.contrib import admin
from django.utils.safestring import mark_safe
from events.models import Event


class OrganizationInline(admin.TabularInline):
    model = Event.organizations.through
    extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "date",
        "get_image",
        "get_organization",
    )
    inlines = [OrganizationInline]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src={obj.image.url} width="60" height="60"'
            )
        return "----"

    get_image.short_description = "Изображение"

    def get_organization(self, obj):
        if obj.organizations:
            return ",\n".join([p.title for p in obj.organizations.all()])
        return "----"

    get_organization.short_description = "Организации"
    save_on_top = True
    list_filter = ("date",)
    search_fields = ("id", "title", "date")
