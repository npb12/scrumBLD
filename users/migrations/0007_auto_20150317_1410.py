# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20150317_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associate',
            name='requested',
            field=models.ForeignKey(related_name='requested_user', verbose_name=b'Which user would they like to connect with?', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='associate',
            name='requesting',
            field=models.ForeignKey(related_name='requesting_user', verbose_name=b'Who is making the request?', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='dateSent',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 17, 14, 10, 42, 626041), verbose_name=b'Date Sent'),
            preserve_default=True,
        ),
    ]
