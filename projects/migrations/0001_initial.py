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
                ('title', models.CharField(max_length=144, verbose_name=b'Project Name')),
                ('description', models.CharField(max_length=500, verbose_name=b'Project Description')),
                ('details', models.TextField(verbose_name=b'Project Details')),
                ('createdOn', models.DateField(default=datetime.datetime(2015, 3, 22, 3, 30, 58, 824780), verbose_name=b'Date Created')),
                ('isPrivate', models.BooleanField(default=False, verbose_name=b'Private')),
                ('createdBy', models.ForeignKey(verbose_name=b'Creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('requestedOn', models.DateField(default=datetime.datetime(2015, 3, 22, 3, 30, 58, 825713), verbose_name=b'Date requested')),
                ('isRequestAccepted', models.BooleanField(default=False, verbose_name=b'Request Accepted?')),
                ('requestedBy', models.ForeignKey(verbose_name=b'Which Users?', to=settings.AUTH_USER_MODEL)),
                ('requestedProject', models.ForeignKey(verbose_name=b'Which project?', to='projects.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('needsJavaDev', models.BooleanField(default=False, verbose_name=b'Java')),
                ('needsFrontEndDev', models.BooleanField(default=False, verbose_name=b'Frontend Dev')),
                ('needsMarketing', models.BooleanField(default=False, verbose_name=b'Marketing')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
