# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_auto_20151120_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='venue_Company',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='venue_Rating',
            field=models.IntegerField(null=True),
        ),
    ]
