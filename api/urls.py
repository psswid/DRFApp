"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .views import FacebookLogin, TwitterLogin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("rest-auth/", include("rest_auth.urls")),
    path("hijack/", include("hijack.urls", namespace="hijack")),
    path("rest-auth/facebook/", FacebookLogin.as_view(), name="fb_login"),
    path("rest-auth/twitter/", TwitterLogin.as_view(), name="twitter_login"),
    path("", include("api.apps.blog.urls")),
    path("", include("api.apps.articles.urls")),
    path("", include("api.apps.comments.urls")),
    path("", include("api.apps.users.urls")),
    path("", include("api.apps.products.urls")),
    path("", include("api.apps.cart.urls")),
]
