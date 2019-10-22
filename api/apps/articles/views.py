from rest_framework import generics, viewsets, status
from rest_framework.permissions import (AllowAny, IsAdminUser)
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Article
from .renderers import ArticleJSONRenderer
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    renderer_classes = (ArticleJSONRenderer,)
    permission_classes = [AllowAny,]

    def get_queryset(self):
        return Article.objects

    @action(detail=False, methods=['get'])
    def get_sorted_by_pub_date(self, *args):
        queryset = self.get_queryset().sort_by_pub_date()
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response({'entries': serializer.data}, status=status.HTTP_200_OK)


