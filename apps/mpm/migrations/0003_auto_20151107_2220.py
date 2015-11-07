# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0002_auto_20151107_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoria_mae',
            field=models.ForeignKey(to='mpm.Categoria', null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='musicas',
            field=models.ManyToManyField(to='mpm.Musica', null=True),
        ),
    ]
