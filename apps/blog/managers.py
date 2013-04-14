from django.db import models


class EntryManager(models.Manager):
	def valids(self):
		return self.get_query_set().exclude(draft=True)