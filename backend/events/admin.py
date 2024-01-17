from django.contrib import admin


from events.models import Event


@admin.register(Event)
class OrganizationAdmin(admin.ModelAdmin):
    """Огранизация"""

    list_display = (
        "id",
        "title",
        "image",
        "date",
    )
    save_on_top = True
    list_filter = ("date",)
    search_fields = ("id", "title", "date")
