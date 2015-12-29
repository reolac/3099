# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('venue_Name', models.CharField(max_length=45)),
                ('venue_Location', models.CharField(max_length=45)),
                ('venue_Description', models.CharField(max_length=250)),
                ('venue_Category', models.CharField(max_length=15)),
                ('venue_Rating', models.IntegerField()),
                ('venue_Updated', models.DateTimeField(verbose_name='date published')),
                ('venue_Owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
