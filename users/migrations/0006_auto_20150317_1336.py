# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150316_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='associate',
            name='dateRemoved',
            field=models.DateField(null=True, verbose_name=b'Date Removed', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='associate',
            name='dateRequested',
            field=models.DateField(default=datetime.date(2015, 3, 17), verbose_name=b'Date Requested'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='dateSent',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 17, 13, 36, 36, 38760), verbose_name=b'Date Sent'),
            preserve_default=True,
        ),
    ]
