# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-28 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0002_auto_20160303_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='votes',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='musica',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]