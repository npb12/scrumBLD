# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150312_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='testField',
            field=models.TextField(default=b'Hello test field', verbose_name=b'Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='createdOn',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 20, 11, 17, 887639), verbose_name=b'Date Created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requests',
            name='requestedOn',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 20, 11, 17, 888204), verbose_name=b'Date requested'),
            preserve_default=True,
        ),
    ]
