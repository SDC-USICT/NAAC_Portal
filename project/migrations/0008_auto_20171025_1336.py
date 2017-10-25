# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20170903_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='copi',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Co Principle Investigators'),
        ),
        migrations.RemoveField(
            model_name='projects',
            name='author',
        ),
        migrations.AddField(
            model_name='projects',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Principle Investigator'),
        ),
    ]