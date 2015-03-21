# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150319_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='dateAccepted',
            field=models.DateField(default=datetime.date(2015, 3, 20), verbose_name=b'Date Accepted'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='friend',
            name='dateRequested',
            field=models.DateField(default=datetime.date(2015, 3, 20), verbose_name=b'Date Requested'),
            preserve_default=True,
        ),
    ]
