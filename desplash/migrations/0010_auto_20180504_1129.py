# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-04 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desplash', '0009_category_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ManyToManyField(blank=True, to='desplash.Image'),
        ),
    ]
