# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 23:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects_taken', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='subject',
            table='subject',
        ),
        migrations.AlterModelTable(
            name='subjectstaken',
            table='subjects_taken',
        ),
    ]
