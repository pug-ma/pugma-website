from django.views.generic import ListView

from apps.blog.models import Entry


class IndexView(ListView):
	queryset = Entry.objects.valids()
	template_name = 'base.html'