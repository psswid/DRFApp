from __future__ import absolute_import, unicode_literals
from celery import shared_task

from api.apps.articles.models import Article
from api.apps.blog.models import Entry


@shared_task
def count_comments(obj_url):
    """Celery comments counter changing comments count for related Comment entity"""
    url = obj_url["comment_object"]
    id = url[-1]
    if "articles" in url:
        article = Article.objects.get(id=id)
        Article.objects.filter(id=id).update(comments_count=article.comments.all().count())
    elif "entries" in url:
        entry = Entry.objects.get(id=id)
        Entry.objects.filter(id=id).update(comments_count=entry.comments.all().count())
