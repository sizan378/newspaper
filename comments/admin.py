from django.contrib import admin
from .models import Comments


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("comment", "author", "news", "parent")
    list_filter = [
        "author",
        "news",
        "parent",
    ]
    search_fields = [
        "comment",
        "author",
        "news",
        "parent",
    ]


admin.site.register(Comments, CommentsAdmin)
