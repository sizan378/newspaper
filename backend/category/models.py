from django.db import models
from utils.models import TimeStampedModel

class CategoryModel(TimeStampedModel):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name