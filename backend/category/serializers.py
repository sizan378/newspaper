from .models import CategoryModel
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"