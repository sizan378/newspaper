from django.db import models
from utils.models import TimeStamped
from user.models import CustomUser
from newspost.models import News


class Comments(TimeStamped):
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    news = models.ForeignKey(News, on_delete=models.DO_NOTHING)
    parent = models.ForeignKey(
        "self", on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        return self.comment
