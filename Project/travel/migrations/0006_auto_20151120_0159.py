# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_auto_20151120_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinemalocs',
            name='location',
            field=models.CharField(max_length=45),
        ),
    ]
