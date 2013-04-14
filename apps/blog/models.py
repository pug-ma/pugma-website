from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField
from tagging.fields import TagField

from .managers import EntryManager


class Entry(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('author'))
    timestamp = models.DateTimeField(_('timestamp'), auto_now_add=True)
    title = models.CharField(_('title'), max_length=255)
    body = models.TextField(_('body'))
    pub_date = models.DateTimeField(_('publication date'))
    draft = models.BooleanField(_('draft'))
    is_event = models.BooleanField(_('is event'))
    tags = TagField()
    slug = AutoSlugField(populate_from='title', unique_with=('pub_date', ))

    objects = EntryManager()

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __unicode__(self):
        return unicode(self.title)

    @models.permalink
    def get_absolute_url(self):
        args = [
            self.pub_date.strftime("%Y"),
            self.pub_date.strftime("%m"),
            self.pub_date.strftime("%d"),
            self.slug
        ]
        return ('blog_archive_date_detail', args)

