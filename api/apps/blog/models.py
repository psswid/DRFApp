from datetime import datetime
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from api.apps.core.models import BaseModel
from api.apps.comments.models import Comment


class EntryManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(pub_date__lte=datetime.now()).order_by('-pub_date')


class Entry(BaseModel):

    title = models.CharField(db_index=True, max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    comments_count = models.IntegerField(default=0)
    comments = GenericRelation(Comment)

    objects = EntryManager()

    def __str__(self):
        return self.title
