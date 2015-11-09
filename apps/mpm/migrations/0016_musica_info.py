# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0015_categoria_ordem'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='info',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
