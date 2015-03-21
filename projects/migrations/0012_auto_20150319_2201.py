# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20150318_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='details',
            field=models.TextField(default='1', verbose_name=b'Details'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='isPrivate',
            field=models.BooleanField(default=False, verbose_name=b'Private'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='createdOn',
            field=models.DateField(default=datetime.datetime(2015, 3, 19, 21, 59, 31, 903062), verbose_name=b'Date Created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=500, verbose_name=b'Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=144, verbose_name=b'Project Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requests',
            name='requestedOn',
            field=models.DateField(default=datetime.datetime(2015, 3, 19, 21, 59, 31, 905757), verbose_name=b'Date requested'),
            preserve_default=True,
        ),
    ]
