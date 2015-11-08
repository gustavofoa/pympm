# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0009_auto_20151108_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemliturgia',
            name='diaLiturgido',
            field=models.ForeignKey(default=1, to='mpm.DiaLiturgico'),
            preserve_default=False,
        ),
    ]
