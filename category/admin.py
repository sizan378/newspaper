from django.contrib import admin
from .models import CategoryModel


class CategoryAdminModel(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")

admin.site.register(CategoryModel, CategoryAdminModel)
