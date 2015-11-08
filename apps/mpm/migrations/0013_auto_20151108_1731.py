# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0012_itemliturgia_posicao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leitura',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sugestaomusica',
            name='id',
        ),
        migrations.AlterField(
            model_name='leitura',
            name='itemLiturgia',
            field=models.OneToOneField(primary_key=True, serialize=False, to='mpm.ItemLiturgia'),
        ),
        migrations.AlterField(
            model_name='sugestaomusica',
            name='avulsas',
            field=models.ManyToManyField(related_name='SugestoesAvulsas', null=True, to='mpm.Musica'),
        ),
        migrations.AlterField(
            model_name='sugestaomusica',
            name='categorias',
            field=models.ManyToManyField(to='mpm.Categoria', null=True),
        ),
        migrations.AlterField(
            model_name='sugestaomusica',
            name='itemLiturgia',
            field=models.OneToOneField(primary_key=True, serialize=False, to='mpm.ItemLiturgia'),
        ),
        migrations.AlterField(
            model_name='sugestaomusica',
            name='remover',
            field=models.ManyToManyField(related_name='MusicasARemover', null=True, to='mpm.Musica'),
        ),
    ]
