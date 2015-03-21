# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20150314_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='createdOn',
            field=models.DateField(default=datetime.datetime(2015, 3, 16, 8, 41, 12, 89390), verbose_name=b'Date Created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requests',
            name='requestedOn',
            field=models.DateField(default=datetime.datetime(2015, 3, 16, 8, 41, 12, 90619), verbose_name=b'Date requested'),
            preserve_default=True,
        ),
    ]
