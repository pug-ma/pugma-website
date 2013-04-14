from django.contrib import admin

from .models import Entry
from .forms import EntryForm


class EntryAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date')
	list_filter = ('pub_date', )
	form = EntryForm


admin.site.register(Entry, EntryAdmin)