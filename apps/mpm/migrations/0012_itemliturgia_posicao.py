# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0011_auto_20151108_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemliturgia',
            name='posicao',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
