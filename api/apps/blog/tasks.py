from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .models import Entry


# @shared_task
# def count_widgets():
#     return Widget.objects.count()


@shared_task
def count_comments(entry_id):
    # w = Widget.objects.get(id=widget_id)
    # w.name = name
    # w.save()
    entry = Entry.objects.get(id=entry_id)
    entry.comments_count = entry.comments.count()
    entry.save()
