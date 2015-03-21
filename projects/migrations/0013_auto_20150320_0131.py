# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20150319_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='skill',
            field=models.CharField(default='1', max_length=60, verbose_name=b'Skill'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='createdOn',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 1, 31, 4, 820878), verbose_name=b'Date Created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=500, verbose_name=b'Project Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='details',
            field=models.TextField(verbose_name=b'Project Details'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requests',
            name='requestedOn',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 1, 31, 4, 823187), verbose_name=b'Date requested'),
            preserve_default=True,
        ),
    ]
