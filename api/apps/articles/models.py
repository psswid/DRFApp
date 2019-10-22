from django.db import models

from api.apps.core.models import BaseModel


class ArticleQuerySet(models.QuerySet):

    def pub_date(self):
        return self.order_by('-pub_date')


class ArticleManager(models.Manager):

    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def sort_by_pub_date(self):
        return self.get_queryset().pub_date()


class Article(BaseModel):

    title = models.CharField(db_index=True, max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField(null=True)
    comments_count = models.IntegerField(default=0)

    objects = ArticleManager()

    def __str__(self):
        return self.title
