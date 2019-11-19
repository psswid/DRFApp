from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    fields = ["body", "content_type", "object_id"]


admin.site.register(Comment, CommentAdmin)
