# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-29 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0003_auto_20160328_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='destaque',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
