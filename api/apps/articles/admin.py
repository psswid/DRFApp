from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'body']


admin.site.register(Article, ArticleAdmin)
