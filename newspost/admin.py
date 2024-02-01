from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "views", "published_date", "is_published")
    list_filter = [
        "author",
        "category",
    ]
    search_fields = [
        "title",
        "author",
        "category",
    ]

admin.site.register(News, NewsAdmin)