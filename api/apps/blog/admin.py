from django.contrib import admin

from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    fields = ['title', 'body', 'pub_date']


admin.site.register(Entry, EntryAdmin)
