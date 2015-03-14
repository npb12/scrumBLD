# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('requestedOn', models.DateField(default=datetime.datetime(2015, 3, 12, 13, 47, 14, 604191), verbose_name=b'Date requested')),
                ('isRequestAccepted', models.BooleanField(default=False, verbose_name=b'Request Accepted?')),
                ('requestedBy', models.ForeignKey(verbose_name=b'Which Users?', to=settings.AUTH_USER_MODEL)),
                ('requestedProject', models.ForeignKey(verbose_name=b'Which project?', to='projects.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='project',
            name='createdOn',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 13, 47, 14, 603663), verbose_name=b'Date Created'),
            preserve_default=True,
        ),
    ]
