from pprint import pprint

from rest_framework import generics, viewsets, status
from rest_framework.exceptions import NotFound
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
        return Entry.objects

    @action(detail=False, methods=['get'])
    def get_sorted_by_pub_date(self, *args):
        queryset = self.get_queryset().sort_by_pub_date()
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response({'entries': serializer.data}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['put'])
    def set_publicated(self, request, entry_pk=None):
        try:
            entry = Entry.objects.get(pk=entry_pk)
        except Entry.DoesNotExist:
            raise NotFound("Entry not found.")

        entry.pub_date()

