from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Address

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("email", "username", "is_staff", "is_verified")
    search_fields = ("email", "username")
    ordering = ("-date_joined",)
    
    # Add your custom fields to the fieldsets
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("phone_number", "is_verified", "is_first_login", "is_blocked")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("email", "phone_number", "is_verified", "is_first_login", "is_blocked")}),
    )

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "user", "city", "state", "is_default")
    list_filter = ("state", "is_default")
    search_fields = ("full_name", "city", "postal_code")

