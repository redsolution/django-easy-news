# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'News'
        db.create_table('easy_news_news', (
            ('short', self.gf('tinymce.models.HTMLField')(default='', blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('tinymce.models.HTMLField')(default='', blank=True)),
            ('show', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, db_index=True)),
        ))
        db.send_create_signal('easy_news', ['News'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'News'
        db.delete_table('easy_news_news')
    
    
    models = {
        'easy_news.news': {
            'Meta': {'object_name': 'News'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short': ('tinymce.models.HTMLField', [], {'default': "''", 'blank': 'True'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'db_index': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {'default': "''", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }
    
    complete_apps = ['easy_news']
