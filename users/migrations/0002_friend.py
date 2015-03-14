# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateRequested', models.DateField(default=datetime.date(2015, 3, 14), verbose_name=b'Date Requested')),
                ('dateAccepted', models.DateField(default=datetime.date(2015, 3, 14), verbose_name=b'Date Accepted')),
                ('requested', models.ForeignKey(related_name='requested_user', verbose_name=b'Requested User', to=settings.AUTH_USER_MODEL)),
                ('requesting', models.ForeignKey(related_name='requesting_user', verbose_name=b'Requesting User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
