from .models import CategoryModel
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from .serializers import CategorySerializer


class CategoryListCreateView(ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateView(UpdateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
