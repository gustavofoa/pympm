# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0005_auto_20151107_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='musicas',
        ),
    ]
