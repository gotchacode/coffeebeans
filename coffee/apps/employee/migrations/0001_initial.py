# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Employee'
        db.create_table(u'employee_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('employee_code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_of_joining', self.gf('django.db.models.fields.DateField')()),
            ('salary', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'employee', ['Employee'])


    def backwards(self, orm):
        # Deleting model 'Employee'
        db.delete_table(u'employee_employee')


    models = {
        u'employee.employee': {
            'Meta': {'object_name': 'Employee'},
            'date_of_joining': ('django.db.models.fields.DateField', [], {}),
            'employee_code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'salary': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['employee']