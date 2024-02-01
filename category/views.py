from .models import CategoryModel
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .serializers import CategorySerializer


class AdminCategoryListCreateView(ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class AdminCategoryUpdateView(RetrieveUpdateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
