# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_auto_20151120_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinemalocs',
            name='location',
            field=models.CharField(unique=True, max_length=45),
        ),
    ]
