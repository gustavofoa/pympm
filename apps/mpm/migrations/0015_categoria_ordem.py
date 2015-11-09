# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0014_auto_20151108_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='ordem',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
