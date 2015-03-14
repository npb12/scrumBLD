# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20150312_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='testField',
        ),
        migrations.AlterField(
            model_name='project',
            name='createdOn',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 20, 12, 32, 886193), verbose_name=b'Date Created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requests',
            name='requestedOn',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 20, 12, 32, 886761), verbose_name=b'Date requested'),
            preserve_default=True,
        ),
    ]
