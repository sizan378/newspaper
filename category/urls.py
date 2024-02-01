from django.urls import path
from .views import AdminCategoryListCreateView, AdminCategoryUpdateView

urlpatterns = [
    path(
        route="list-create/",
        view=AdminCategoryListCreateView.as_view(),
        name="category_list_create",
    ),
    path(
        route="update/<int:pk>",
        view=AdminCategoryUpdateView.as_view(),
        name="category_update",
    ),
]
