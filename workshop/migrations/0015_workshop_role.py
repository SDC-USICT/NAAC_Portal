# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-10 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0014_merge_20171109_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='role',
            field=models.CharField(default=21, max_length=100, verbose_name=b'Role'),
            preserve_default=False,
        ),
    ]
