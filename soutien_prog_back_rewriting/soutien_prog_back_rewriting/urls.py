"""soutien_prog_back_rewriting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import os

from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from rest_framework_simplejwt import views as jwt_views
from .views import (
    CustomTokenObtainPairView,
    TokenVerifyViewWithCookie,
    LogoutWithCookie,
    UserView
)

urls = [
    path("user/", UserView().as_view()),
    path("auth/", CustomTokenObtainPairView().as_view()),
    path("refresh/", jwt_views.TokenRefreshView().as_view()),
    path("verify/", TokenVerifyViewWithCookie().as_view()),
    path("logout/", LogoutWithCookie().as_view()),
    path("course/", include("course.urls")),
    path("module/", include("schoolmodule.urls")),
    path("participant/", include("participant.urls")),
]

if os.environ.get("USE_NGINX") == 1:
    urlpatterns = [
        path("admin/", admin.site.urls),
        *urls  
    ]

else:
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("api/", include(urls))
    ]