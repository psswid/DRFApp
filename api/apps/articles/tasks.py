from __future__ import absolute_import, unicode_literals
from django.db.models import Count
from celery import shared_task
from .models import Article
from api.apps.comments.models import Comment
from pprint import pprint

# @shared_task
# def count_widgets():
#     return Widget.objects.count()

# do przerobienia, bo ma sie robic count kiedy zostaje dodany komentarz, ja to wywołue przy get artykułu, to do pizdy
# co na zasadzie sprawdzania czy pobrany z id obiekt jest instancją articles to wtedy comments count articles jak nie wpisów i powino byc ok
@shared_task
def count_comments(article_id):
    article = Article.objects.get(id=article_id)
    comments = article.comments.all().count()
    article.comments_count = comments
    article.save()
