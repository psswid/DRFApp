from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import User
from .renderers import UserJSONRenderer
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = (UserJSONRenderer,)
    permission_classes = [
        AllowAny,
    ]

    def get_queryset(self):
        return User.objects
