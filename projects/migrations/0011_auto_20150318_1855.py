# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20150316_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='createdOn',
            field=models.DateField(default=datetime.datetime(2015, 3, 18, 18, 55, 32, 233470), verbose_name=b'Date Created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requests',
            name='requestedOn',
            field=models.DateField(default=datetime.datetime(2015, 3, 18, 18, 55, 32, 234898), verbose_name=b'Date requested'),
            preserve_default=True,
        ),
    ]
