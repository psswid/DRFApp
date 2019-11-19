from __future__ import absolute_import, unicode_literals
from celery import shared_task

from api.apps.articles.models import Article
from api.apps.blog.models import Entry


@shared_task
def count_comments(obj_url):
    url = obj_url["comment_object"]
    id = url[-1]
    if "articles" in url:
        article = Article.objects.get(id=id)
        comments_count = article.comments.all().count()
        article.comments_count = comments_count
        article.save()
    if "entries" in url:
        entry = Entry.objects.get(id=id)
        comments_count = entry.comments.all().count()
        entry.comments_count = comments_count
        entry.save()
