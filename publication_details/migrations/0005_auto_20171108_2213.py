# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-08 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_details', '0004_auto_20171107_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalpapers',
            name='hindex',
            field=models.IntegerField(verbose_name='H-Index of Journal using Scimago (if Scopus, SCI-Ex or SCI)'),
        ),
        migrations.AlterField(
            model_name='journalpapers',
            name='impact_factor',
            field=models.IntegerField(verbose_name='Impact Factor if SCI-Ex or SCI'),
        ),
        migrations.AlterField(
            model_name='journalpapers',
            name='publisher',
            field=models.CharField(max_length=100, verbose_name='Journal Name with Publisher'),
        ),
    ]