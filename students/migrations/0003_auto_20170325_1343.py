# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-25 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20170325_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=255, verbose_name='адрес'),
        ),
    ]
