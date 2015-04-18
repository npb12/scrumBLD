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
            name='Associate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateRequested', models.DateField(default=datetime.date(2015, 3, 21), verbose_name=b'Date Requested')),
                ('dateAccepted', models.DateField(null=True, verbose_name=b'Date Accepted', blank=True)),
                ('dateRemoved', models.DateField(null=True, verbose_name=b'Date Removed', blank=True)),
                ('requested', models.ForeignKey(related_name='requested_user', verbose_name=b'Which user would they like to connect with?', to=settings.AUTH_USER_MODEL)),
                ('requesting', models.ForeignKey(related_name='requesting_user', verbose_name=b'Who is making the request?', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(verbose_name=b'Message')),
                ('dateSent', models.DateTimeField(default=datetime.datetime(2015, 3, 21, 14, 18, 45, 95563), verbose_name=b'Date Sent')),
                ('isSeen', models.BooleanField(default=False, verbose_name=b'Seen?')),
                ('fromUser', models.ForeignKey(related_name='from_user', verbose_name=b'From', to=settings.AUTH_USER_MODEL)),
                ('toUser', models.ForeignKey(related_name='to_user', verbose_name=b'To', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastConvo', models.CharField(max_length=5, null=True, verbose_name=b'PK of last conversation', blank=True)),
                ('github', models.URLField(null=True, verbose_name=b'GitHub Account', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
            bases=(models.Model,),
        ),
    ]
