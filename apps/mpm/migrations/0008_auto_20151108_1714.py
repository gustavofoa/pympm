# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0007_auto_20151108_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='data',
            new_name='dia',
        ),
    ]
