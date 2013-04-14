from django.db import models
from django.utils.translation import ugettext_lazy as _


from tagging.fields import TagField

from .managers import EntryManager


class Entry(models.Model):
	timestamp = models.DateTimeField(_('timestamp'), auto_now_add=True)
	title = models.CharField(_('title'), max_length=255)
	body = models.TextField(_('body'))
	pub_date = models.DateTimeField(_('publication date'))
	draft = models.BooleanField(_('draft'))
	tags = TagField()

	objects = EntryManager()

	class Meta:
		verbose_name = _('post')
		verbose_name_plural = _('posts')

	def __unicode__(self):
		return unicode(self.title)


