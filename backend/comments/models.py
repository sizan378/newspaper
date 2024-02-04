from django.db import models
from utils.models import TimeStamped
from user.models import CustomUser
from newspost.models import News
from django.conf import settings

class Comments(TimeStamped):
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True)
    news = models.ForeignKey(News, on_delete=models.DO_NOTHING)
    parent = models.ForeignKey(
        "self", on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        return self.comment
