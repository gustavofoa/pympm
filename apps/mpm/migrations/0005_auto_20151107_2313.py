# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0004_auto_20151107_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='link_video',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='musica',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
