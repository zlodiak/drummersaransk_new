# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table('app_drummersaransk_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
        ))
        db.send_create_signal('app_drummersaransk', ['City'])

        # Adding model 'Status'
        db.create_table('app_drummersaransk_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('app_drummersaransk', ['Status'])

        # Adding model 'Gender'
        db.create_table('app_drummersaransk_gender', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal('app_drummersaransk', ['Gender'])

        # Adding model 'Teacher'
        db.create_table('app_drummersaransk_teacher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teacher', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('app_drummersaransk', ['Teacher'])

        # Adding model 'UserProfile'
        db.create_table('app_drummersaransk_userprofile', (
            ('user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, unique=True, to=orm['auth.User'])),
            ('family', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True, null=True)),
            ('name1', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True, null=True)),
            ('name2', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True, null=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gender', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['app_drummersaransk.Gender'], null=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['app_drummersaransk.Status'], null=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, max_length=50, to=orm['app_drummersaransk.City'], null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True, null=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True, null=True)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('other', self.gf('django.db.models.fields.TextField')(max_length=500, blank=True, null=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True)),
            ('drum_period_1', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('drum_period_2', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('drum_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True)),
            ('drums', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True, null=True)),
            ('cymbals', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True, null=True)),
            ('hardware', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True, null=True)),
            ('sticks', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True, null=True)),
            ('plastics', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True, null=True)),
            ('groups_past', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True, null=True)),
            ('groups_present', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True, null=True)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['app_drummersaransk.Teacher'], null=True)),
            ('teacher_fio', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True, null=True)),
            ('drummers', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True, null=True)),
        ))
        db.send_create_signal('app_drummersaransk', ['UserProfile'])

        # Adding model 'PathGlory'
        db.create_table('app_drummersaransk_pathglory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True, null=True)),
            ('teaser', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('path_glory_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True)),
        ))
        db.send_create_signal('app_drummersaransk', ['PathGlory'])

        # Adding model 'Friends'
        db.create_table('app_drummersaransk_friends', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('friend_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('app_drummersaransk', ['Friends'])

        # Adding model 'Message'
        db.create_table('app_drummersaransk_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sender', to=orm['auth.User'])),
            ('reciever', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recipient', to=orm['auth.User'])),
            ('date_send', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_recieve', self.gf('django.db.models.fields.DateTimeField')(blank=True, null=True)),
            ('theme', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True, null=True)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('sender_show', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('reciever_show', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('app_drummersaransk', ['Message'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table('app_drummersaransk_city')

        # Deleting model 'Status'
        db.delete_table('app_drummersaransk_status')

        # Deleting model 'Gender'
        db.delete_table('app_drummersaransk_gender')

        # Deleting model 'Teacher'
        db.delete_table('app_drummersaransk_teacher')

        # Deleting model 'UserProfile'
        db.delete_table('app_drummersaransk_userprofile')

        # Deleting model 'PathGlory'
        db.delete_table('app_drummersaransk_pathglory')

        # Deleting model 'Friends'
        db.delete_table('app_drummersaransk_friends')

        # Deleting model 'Message'
        db.delete_table('app_drummersaransk_message')


    models = {
        'app_drummersaransk.city': {
            'Meta': {'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
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
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'app_drummersaransk.message': {
            'Meta': {'object_name': 'Message'},
            'date_recieve': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'date_send': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reciever': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipient'", 'to': "orm['auth.User']"}),
            'reciever_show': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sender'", 'to': "orm['auth.User']"}),
            'sender_show': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'theme': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'})
        },
        'app_drummersaransk.pathglory': {
            'Meta': {'object_name': 'PathGlory'},
            'date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path_glory_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
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
            'Meta': {'object_name': 'UserProfile', '_ormbases': ['auth.User']},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'max_length': '50', 'to': "orm['app_drummersaransk.City']", 'null': 'True'}),
            'cymbals': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True', 'null': 'True'}),
            'drum_period_1': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'drum_period_2': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'drum_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'drummers': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True', 'null': 'True'}),
            'drums': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True', 'null': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'family': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['app_drummersaransk.Gender']", 'null': 'True'}),
            'groups_past': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True', 'null': 'True'}),
            'groups_present': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True', 'null': 'True'}),
            'hardware': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True', 'null': 'True'}),
            'name1': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'}),
            'name2': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'other': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'plastics': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True', 'null': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['app_drummersaransk.Status']", 'null': 'True'}),
            'sticks': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True', 'null': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['app_drummersaransk.Teacher']", 'null': 'True'}),
            'teacher_fio': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True', 'null': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Group']", 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']", 'related_name': "'user_set'"}),
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