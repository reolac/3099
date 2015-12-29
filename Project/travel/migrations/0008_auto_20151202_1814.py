# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0007_auto_20151120_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='venue_Company',
        ),
        migrations.AddField(
            model_name='venue',
            name='venue_Logo',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
