# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Entry.tags'
        db.add_column(u'blog_entry', 'tags',
                      self.gf('tagging.fields.TagField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Entry.tags'
        db.delete_column(u'blog_entry', 'tags')


    models = {
        u'blog.entry': {
            'Meta': {'object_name': 'Entry'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'tags': ('tagging.fields.TagField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']