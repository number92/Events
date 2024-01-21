from django.contrib import admin
from organizations.models import Organization, Membership


# @admin.register(Membership)
class MembershipInlines(admin.TabularInline):
    model = Membership
    extra = 1


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
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
    inlines = [
        MembershipInlines,
    ]
    ordering = ("id",)


@admin.register(Membership)
class MemberShipAdmin(admin.ModelAdmin):
    list_display = ("id", "organization", "user")
    list_editable = ("organization", "user")
    list_filter = ("organization",)
