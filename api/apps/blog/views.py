from rest_framework import generics, viewsets, status
from rest_framework.permissions import (AllowAny, IsAdminUser)
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Entry
from .renderers import EntryJSONRenderer
from .serializers import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    renderer_classes = (EntryJSONRenderer,)
    permission_classes = [AllowAny,]

    def get_queryset(self):
        return Entry.objects.all()


