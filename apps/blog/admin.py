from django.contrib import admin

from .models import Entry
from .forms import EntryForm


class EntryAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date')
	list_filter = ('pub_date', )
	form = EntryForm

	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()


admin.site.register(Entry, EntryAdmin)