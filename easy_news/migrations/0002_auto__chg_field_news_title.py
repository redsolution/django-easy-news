# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'News.title'
        db.alter_column('easy_news_news', 'title', self.gf('django.db.models.fields.CharField')(max_length=500))
    
    
    def backwards(self, orm):
        
        # Changing field 'News.title'
        db.alter_column('easy_news_news', 'title', self.gf('django.db.models.fields.CharField')(max_length=200))
    
    
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
    
    complete_apps = ['easy_news']
