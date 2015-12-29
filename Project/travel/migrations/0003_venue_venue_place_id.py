# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20151113_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='venue_Place_ID',
            field=models.CharField(default=datetime.datetime(2015, 11, 18, 21, 36, 41, 281886, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
    ]
