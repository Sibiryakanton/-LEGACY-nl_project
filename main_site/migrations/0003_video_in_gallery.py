# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-21 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0002_auto_20170408_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='in_gallery',
            field=models.BooleanField(default=False, verbose_name='Показывать в разделе "Видео"'),
        ),
    ]
