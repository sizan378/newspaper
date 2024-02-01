from django.contrib import admin
from .models import CustomUser


class AdminCustomUser(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "phone_number", "address", "is_staff", "is_active", "date_joined")
    list_filter = [
        "is_staff",
        "is_active",
    ]
    search_fields = [
        "email",
        "first_name",
        "last_name",
        "phone_number",
    ]

admin.site.register(CustomUser, AdminCustomUser)
