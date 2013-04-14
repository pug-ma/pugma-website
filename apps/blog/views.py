from django.http import Http404
from django.views.generic import DetailView, ListView

from tagging.models import Tag
from tagging.models import TaggedItem

from .models import Entry


class TaggedEntryListView(ListView):
    model = Entry

    def get_queryset(self):
        return TaggedItem.objects.get_by_model(Entry, Tag.objects.filter(name__in=[self.kwargs['tag']]))


class EntryDetailView(DetailView):
    """Detail for an ``Entry``."""
    model = Entry
    slug_field = 'slug'

    def get_object(self, **kwargs):
        """Make sure the ``Entry`` contains the correct date if it was
        specified."""
        obj = super(EntryDetailView, self).get_object(**kwargs)

        year = self.kwargs.get('year', None)
        month = self.kwargs.get('month', None)
        day = self.kwargs.get('day', None)

        if year and month and day:
            # IF the dates are different, throw a fit!
            try:
                assert obj.published_on.year == int(year)
                assert obj.published_on.month == int(month)
                assert obj.published_on.day == int(day)
            except AssertionError:
                raise Http404

        return obj