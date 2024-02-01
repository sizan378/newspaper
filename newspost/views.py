from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework import status
from .models import News
from .serializers import NewsSerializer


class AdminNewsListCreateView(ListCreateAPIView):
    queryset = News.objects.all()
    serializers_class = NewsSerializer


class AdminNewsUpdateView(RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializers_class = NewsSerializer


class UserNewsListView(APIView):
    def get(self, request):
        # print("user_id", request.user)
        news = News.objects.filter(author=request.user)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserNewsUpdateDetailsView(APIView):

    def get(self, request, pk):
        try:
            news = News.objects.filter(id=pk)
            if not news:
                return Response(
                    {"message": "News does not exist"}, status=status.HTTP_400_BAD_REQUEST
                )
        except news.DoesNotExist:
            return Response(
                {"message": "News does not exist"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(instance=news, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)