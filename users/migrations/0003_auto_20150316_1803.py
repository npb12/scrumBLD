# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_lastconvo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associate',
            name='dateAccepted',
            field=models.DateField(verbose_name=b'Date Accepted', blank=True),
            preserve_default=True,
        ),
    ]
