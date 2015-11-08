# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0013_auto_20151108_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemliturgia',
            name='descricao',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sugestaomusica',
            name='avulsas',
            field=models.ManyToManyField(related_name='SugestoesAvulsas', null=True, to='mpm.Musica', blank=True),
        ),
        migrations.AlterField(
            model_name='sugestaomusica',
            name='remover',
            field=models.ManyToManyField(related_name='MusicasARemover', null=True, to='mpm.Musica', blank=True),
        ),
    ]
