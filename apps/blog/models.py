from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
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
    tags = TagField()
    slug = AutoSlugField(populate_from='title', unique_with=('pub_date', ))

    objects = EntryManager()

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ('-timestamp', )

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

    def get_full_url(self):
        return ''.join([settings.SITE_PROTOCOL, Site.objects.get_current().domain, self.get_absolute_url()])



