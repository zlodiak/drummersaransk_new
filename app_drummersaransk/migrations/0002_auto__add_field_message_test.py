# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Message.test'
        db.add_column('app_drummersaransk_message', 'test',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Message.test'
        db.delete_column('app_drummersaransk_message', 'test')


    models = {
        'app_drummersaransk.city': {
            'Meta': {'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'app_drummersaransk.friends': {
            'Meta': {'object_name': 'Friends'},
            'friend_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'app_drummersaransk.gender': {
            'Meta': {'object_name': 'Gender'},
            'gender': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'app_drummersaransk.message': {
            'Meta': {'object_name': 'Message'},
            'date_recieve': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'date_send': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reciever': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'recipient'"}),
            'reciever_show': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'sender'"}),
            'sender_show': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'test': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'theme': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'})
        },
        'app_drummersaransk.pathglory': {
            'Meta': {'object_name': 'PathGlory'},
            'date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path_glory_photo': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'place': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'teaser': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'app_drummersaransk.status': {
            'Meta': {'object_name': 'Status'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'app_drummersaransk.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'teacher': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'app_drummersaransk.userprofile': {
            'Meta': {'_ormbases': ['auth.User'], 'object_name': 'UserProfile'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['app_drummersaransk.City']", 'max_length': '50'}),
            'cymbals': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '300'}),
            'drum_period_1': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'drum_period_2': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'drum_photo': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'drummers': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '300'}),
            'drums': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '300'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'family': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['app_drummersaransk.Gender']", 'null': 'True'}),
            'groups_past': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '300'}),
            'groups_present': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '300'}),
            'hardware': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '300'}),
            'name1': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'name2': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'max_length': '500'}),
            'phone': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'plastics': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '300'}),
            'skype': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['app_drummersaransk.Status']", 'null': 'True'}),
            'sticks': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '300'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['app_drummersaransk.Teacher']", 'null': 'True'}),
            'teacher_fio': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '300'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['auth.User']", 'unique': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app_drummersaransk']