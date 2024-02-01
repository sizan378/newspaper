from django.db import models
from user.models import CustomUser
from category.models import CategoryModel
from utils.models import TimeStampedModel


class News(TimeStampedModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING)
    views = models.PositiveIntegerField(default=0)
    published_date = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=False)


    def __str__(self):
        return self.title
