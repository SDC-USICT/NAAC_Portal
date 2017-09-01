# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects_taken', '0002_auto_20170825_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='code',
            field=models.CharField(max_length=100, verbose_name='Subject Code'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='credit',
            field=models.IntegerField(verbose_name='Credit'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Subject Name'),
        ),
        migrations.AlterField(
            model_name='subjectstaken',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee', verbose_name='Employee ID'),
        ),
        migrations.AlterField(
            model_name='subjectstaken',
            name='school',
            field=models.CharField(max_length=100, verbose_name='School'),
        ),
        migrations.AlterField(
            model_name='subjectstaken',
            name='year',
            field=models.CharField(max_length=100, verbose_name='Year'),
        ),
    ]
