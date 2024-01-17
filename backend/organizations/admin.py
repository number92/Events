from django.contrib import admin


from organizations.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """Огранизация"""

    list_display = (
        "id",
        "title",
        "address",
        "postcode",
    )
    save_on_top = True
    search_fields = (
        "id",
        "title",
        "address",
    )
