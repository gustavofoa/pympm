# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sugestaomusica',
            name='categorias',
            field=models.ManyToManyField(related_name='categorias', to='mpm.Categoria'),
        ),
    ]
