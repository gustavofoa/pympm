# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0003_auto_20151107_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoria_mae',
            field=models.ForeignKey(blank=True, to='mpm.Categoria', null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='musicas',
            field=models.ManyToManyField(to='mpm.Musica', null=True, blank=True),
        ),
    ]
