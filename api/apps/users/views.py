from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.permissions import (IsAuthenticated, IsAdminUser, AllowAny)

from .models import User
from .renderers import UserJSONRenderer
from .serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = (UserJSONRenderer,)
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return User.objects
