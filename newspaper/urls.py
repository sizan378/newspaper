"""
URL configuration for newspaper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from .settings.settings import DEBUG
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

""" swagger setup """
schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version="v1",
        description="My API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]

# Third party apps
urlpatterns += [
    path("api/v1/newspost/", include("newspost.urls")),
    path("api/v1/user/", include("user.urls")),
    path("api/v1/comments/", include("comments.urls")),
    path("api/v1/category/", include("category.urls")),
]


if DEBUG:
    urlpatterns += [
        # django debug toolbar url add
        path("__debug__/", include(debug_toolbar.urls)),
        # swagger url endpoints
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
    ]
