# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-04 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desplash', '0004_auto_20180504_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ManyToManyField(to='desplash.Category'),
        ),
    ]
