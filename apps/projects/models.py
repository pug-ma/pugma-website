# -*- coding utf-8 -*-
from django.db import models

class Project(models.Model):
    name = models.CharField(u'Nome', max_length=100)
    description = models.CharField(u'Descricao', max_length=100, blank=True)
    image = models.ImageField(u'Imagem', upload_to='projects', blank=True)
    url = models.URLField(u'URL')

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __unicode__(self):
        return self.name
