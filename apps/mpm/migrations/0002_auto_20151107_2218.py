# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoria_mae',
            field=models.ForeignKey(to='mpm.Categoria'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='musicas',
            field=models.ManyToManyField(to='mpm.Musica'),
        ),
    ]
