# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150316_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associate',
            name='dateAccepted',
            field=models.DateField(null=True, verbose_name=b'Date Accepted', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lastConvo',
            field=models.CharField(max_length=5, null=True, verbose_name=b'PK of last conversation', blank=True),
            preserve_default=True,
        ),
    ]
