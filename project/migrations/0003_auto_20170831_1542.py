# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20170825_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='amnt_sanctioned',
            field=models.CharField(max_length=100, verbose_name='Amount Sanctioned'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='copi',
            field=models.ManyToManyField(related_name='employee_copi', to='employee.Employee', verbose_name='Co Author'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='date_completed',
            field=models.DateField(verbose_name='Date of Completed'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='date_of_award',
            field=models.DateField(verbose_name='Date of Award'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_projects', to='employee.Employee', verbose_name='Employee ID'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='pi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_pi', to='employee.Employee', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='sponsors',
            field=models.CharField(max_length=100, verbose_name='Sponsoring Agency'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.CharField(max_length=100, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Project Title'),
        ),
    ]