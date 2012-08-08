# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Site'
        db.create_table('story_database_site', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('story_database', ['Site'])

        # Adding model 'Page'
        db.create_table('story_database_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('video_background', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story_database.Video_Background'])),
        ))
        db.send_create_signal('story_database', ['Page'])

        # Adding model 'Page_Translation'
        db.create_table('story_database_page_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['story_database.Page'])),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('single_line_description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='Featured Video', null=True, to=orm['story_database.Video'])),
        ))
        db.send_create_signal('story_database', ['Page_Translation'])

        # Adding unique constraint on 'Page_Translation', fields ['parent', 'language_code']
        db.create_unique('story_database_page_translation', ['parent_id', 'language_code'])

        # Adding model 'Video_Background'
        db.create_table('story_database_video_background', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('h264_background', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('ogg_background', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('jpg_background', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('story_database', ['Video_Background'])

        # Adding model 'Tag'
        db.create_table('story_database_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('story_database', ['Tag'])

        # Adding model 'Tag_Translation'
        db.create_table('story_database_tag_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['story_database.Tag'])),
            ('translation', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('story_database', ['Tag_Translation'])

        # Adding unique constraint on 'Tag_Translation', fields ['parent', 'language_code']
        db.create_unique('story_database_tag_translation', ['parent_id', 'language_code'])

        # Adding model 'Video'
        db.create_table('story_database_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('vimeo_id', self.gf('django.db.models.fields.IntegerField')()),
            ('thumbnail', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
        ))
        db.send_create_signal('story_database', ['Video'])

        # Adding M2M table for field tags on 'Video'
        db.create_table('story_database_video_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['story_database.video'], null=False)),
            ('tag', models.ForeignKey(orm['story_database.tag'], null=False))
        ))
        db.create_unique('story_database_video_tags', ['video_id', 'tag_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Tag_Translation', fields ['parent', 'language_code']
        db.delete_unique('story_database_tag_translation', ['parent_id', 'language_code'])

        # Removing unique constraint on 'Page_Translation', fields ['parent', 'language_code']
        db.delete_unique('story_database_page_translation', ['parent_id', 'language_code'])

        # Deleting model 'Site'
        db.delete_table('story_database_site')

        # Deleting model 'Page'
        db.delete_table('story_database_page')

        # Deleting model 'Page_Translation'
        db.delete_table('story_database_page_translation')

        # Deleting model 'Video_Background'
        db.delete_table('story_database_video_background')

        # Deleting model 'Tag'
        db.delete_table('story_database_tag')

        # Deleting model 'Tag_Translation'
        db.delete_table('story_database_tag_translation')

        # Deleting model 'Video'
        db.delete_table('story_database_video')

        # Removing M2M table for field tags on 'Video'
        db.delete_table('story_database_video_tags')


    models = {
        'story_database.page': {
            'Meta': {'object_name': 'Page'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video_background': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story_database.Video_Background']"})
        },
        'story_database.page_translation': {
            'Meta': {'unique_together': "(('parent', 'language_code'),)", 'object_name': 'Page_Translation'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['story_database.Page']"}),
            'single_line_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Featured Video'", 'null': 'True', 'to': "orm['story_database.Video']"})
        },
        'story_database.site': {
            'Meta': {'object_name': 'Site'},
            'domain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'story_database.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'story_database.tag_translation': {
            'Meta': {'unique_together': "(('parent', 'language_code'),)", 'object_name': 'Tag_Translation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['story_database.Tag']"}),
            'translation': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'story_database.video': {
            'Meta': {'object_name': 'Video'},
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['story_database.Tag']", 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'vimeo_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'story_database.video_background': {
            'Meta': {'object_name': 'Video_Background'},
            'h264_background': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jpg_background': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ogg_background': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['story_database']