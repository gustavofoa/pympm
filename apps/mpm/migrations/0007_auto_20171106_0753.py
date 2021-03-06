# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-06 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0006_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='banner_footer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banner_footer_cat', to='mpm.Banner'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='banner_lateral',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banner_lateral_cat', to='mpm.Banner'),
        ),
        migrations.AddField(
            model_name='dialiturgico',
            name='banner_footer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banner_footer_dia', to='mpm.Banner'),
        ),
        migrations.AddField(
            model_name='dialiturgico',
            name='banner_lateral',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banner_lateral_dia', to='mpm.Banner'),
        ),
        migrations.AddField(
            model_name='musica',
            name='banner_footer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banner_footer_mus', to='mpm.Banner'),
        ),
        migrations.AddField(
            model_name='musica',
            name='banner_lateral',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banner_lateral_mus', to='mpm.Banner'),
        ),
    ]
