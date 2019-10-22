from django.db import models

from api.apps.core.models import BaseModel


class EntryQuerySet(models.QuerySet):

    def pub_date(self):
        return self.order_by('-pub_date')


class EntryManager(models.Manager):

    def get_queryset(self):
        return EntryQuerySet(self.model, using=self._db)

    def sort_by_pub_date(self):
        return self.get_queryset().pub_date()


class Entry(BaseModel):

    title = models.CharField(db_index=True, max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField(null=True)
    comments_count = models.IntegerField(default=0)

    objects = EntryManager()

    def __str__(self):
        return self.title
