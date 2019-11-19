from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from api.apps.core.models import BaseModel


class Comment(BaseModel):
    """Generic relation comment model usable in i.e. articles and blog app"""
    body = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    comment_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.body
