from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from tagging.models import Tag
from tagging.models import TaggedItem

from .models import Entry


class LatestEntriesFeed(Feed):
    title = "PUG-MA news feed."
    link = '/feed/rss'
    description = "Updates on changes and additions to pug-ma.com."

    def items(self):
        return Entry.objects.valids()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body


class LatestEntriesByTagFeed(Feed):
    description = "Updates on changes and additions to pug-ma.com."

    def get_object(self, request, tag):
        return get_object_or_404(Tag, name__in=[tag])

    def title(self, obj):
        return "PUG-MA news feed filtered by tag {0}.".format(obj.name)

    def items(self, obj):
        return TaggedItem.objects.get_by_model(Entry, obj)

    def link(self, obj):
        return reverse('blog_entry_filter_tag', args=(obj.name, ))

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body