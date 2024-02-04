from django.urls import path
from .views import (
    AdminNewsListCreateView,
    AdminNewsUpdateView,
    UserNewsListView,
    UserNewsUpdateDetailsView,
)

urlpatterns = [
    path(
        route="list-create/",
        view=AdminNewsListCreateView.as_view(),
        name="news_list_create",
    ),
    path(
        route="update/<int:pk>/", view=AdminNewsUpdateView.as_view(), name="news_update"
    ),
    path(
        route="list-update/<int:pk>/",
        view=UserNewsUpdateDetailsView.as_view(),
        name="user_news_update",
    ),
    path(route="list/", view=UserNewsListView.as_view(), name="user_news_list"),
    path(
        route="single-news/<int:pk>/",
        view=UserNewsUpdateDetailsView.as_view(),
        name="single_news",
    ),
]
