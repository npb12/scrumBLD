# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='lastConvo',
            field=models.CharField(max_length=5, verbose_name=b'PK of last conversation', blank=True),
            preserve_default=True,
        ),
    ]
