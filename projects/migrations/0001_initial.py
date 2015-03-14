# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=144, verbose_name=b'Title')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('createdOn', models.DateField(default=datetime.datetime(2015, 3, 12, 13, 42, 40, 852466), verbose_name=b'Date Created')),
                ('createdBy', models.ForeignKey(verbose_name=b'Creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
    ]
