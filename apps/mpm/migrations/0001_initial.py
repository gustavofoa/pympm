# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('slug', models.SlugField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=500)),
                ('categoria_mae', models.ForeignKey(to='mpm.Categoria', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('slug', models.SlugField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('letra', models.TextField()),
                ('cifra', models.TextField()),
                ('link_video', models.URLField()),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('categorias', models.ManyToManyField(to='mpm.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='musicas',
            field=models.ManyToManyField(to='mpm.Musica', blank=True),
        ),
    ]
