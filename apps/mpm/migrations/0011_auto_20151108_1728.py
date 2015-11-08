# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpm', '0010_itemliturgia_dialiturgido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemliturgia',
            old_name='diaLiturgido',
            new_name='diaLiturgico',
        ),
    ]
