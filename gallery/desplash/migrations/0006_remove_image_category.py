# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-04 07:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desplash', '0005_auto_20180504_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
    ]
