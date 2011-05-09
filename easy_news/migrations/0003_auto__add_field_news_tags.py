# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

from easy_news import settings

class Migration(SchemaMigration):
    
    def forwards(self, orm):

        if settings.NEWS_TAGGING:
            # Adding field 'News.tags'
            db.add_column('easy_news_news', 'tags', self.gf('tagging.fields.TagField')(null=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        if settings.NEWS_TAGGING:
            # Deleting field 'News.tags'
            db.delete_column('easy_news_news', 'tags')
    
    
    models = {
        'easy_news.news': {
            'Meta': {'object_name': 'News'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short': ('tinymce.models.HTMLField', [], {'default': "''", 'blank': 'True'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'db_index': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {'default': "''", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }
    if settings.NEWS_TAGGING:
        models['easy_news.news']['tags'] = ('tagging.fields.TagField', [], {'null': 'True'})
    
    complete_apps = ['easy_news']
