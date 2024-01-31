from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "views", "published_date", "is_published")
    list_filter = [
        "author",
    ]
    search_fields = [
        "title",
        "author",
    ]

admin.site.register(News, NewsAdmin)