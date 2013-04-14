# -*- coding: utf-8 -*-
from django.db import models

class Event(models.Model):
    title = models.CharField(u'Título', max_length=100)
    description = models.CharField(u'Descrição', max_length=200)
    date = models.DateTimeField(u'Data')
    local = models.CharField(u'Local', max_length=100)

    def __unicode__(self):
        return self.title
