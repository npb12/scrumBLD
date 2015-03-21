# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150316_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='dateSent',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 16, 18, 34, 38, 181407), verbose_name=b'Date Sent'),
            preserve_default=True,
        ),
    ]
