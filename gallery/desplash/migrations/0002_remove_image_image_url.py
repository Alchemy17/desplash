# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 17:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desplash', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_url',
        ),
    ]