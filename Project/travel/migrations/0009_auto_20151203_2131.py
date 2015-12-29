# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0008_auto_20151202_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='venue_Site',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='venue_Logo',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
