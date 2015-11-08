# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0006_remove_categoria_musicas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('data', models.DateField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiaLiturgico',
            fields=[
                ('slug', models.SlugField(serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=255)),
                ('introducao', models.TextField()),
                ('ano', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ItemLiturgia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Leitura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marcacao_biblia', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('itemLiturgia', models.OneToOneField(to='mpm.ItemLiturgia')),
            ],
        ),
        migrations.CreateModel(
            name='SugestaoMusica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avulsas', models.ManyToManyField(related_name='SugestoesAvulsas', to='mpm.Musica')),
                ('categorias', models.ManyToManyField(to='mpm.Categoria')),
                ('itemLiturgia', models.OneToOneField(to='mpm.ItemLiturgia')),
                ('remover', models.ManyToManyField(related_name='MusicasARemover', to='mpm.Musica')),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='liturgia',
            field=models.ForeignKey(to='mpm.DiaLiturgico'),
        ),
    ]
