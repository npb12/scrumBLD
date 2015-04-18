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
                ('createdOn', models.DateField(default=datetime.datetime(2015, 3, 22, 15, 54, 28, 637273), verbose_name=b'Date Created')),
                ('isPrivate', models.BooleanField(default=False, verbose_name=b'Private')),
                ('createdBy', models.ForeignKey(verbose_name=b'Creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isNeeded', models.BooleanField(default=False, verbose_name=b'Skill is still needed')),
                ('project', models.ForeignKey(verbose_name=b'Connected Project', to='projects.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('requestedOn', models.DateField(default=datetime.datetime(2015, 3, 22, 15, 54, 28, 638354), verbose_name=b'Date requested')),
                ('isRequestAccepted', models.BooleanField(default=False, verbose_name=b'Request Accepted?')),
                ('requestedBy', models.ForeignKey(verbose_name=b'Which Users?', to=settings.AUTH_USER_MODEL)),
                ('requestedProject', models.ForeignKey(verbose_name=b'Which project?', to='projects.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abbreviation', models.CharField(default=b'??', max_length=20, verbose_name=b'Abbreviated Name for Tags')),
                ('fullName', models.CharField(default=b'Name', max_length=100, verbose_name=b'Full skill name')),
                ('description', models.TextField(null=True, verbose_name=b'Description of Skill', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateJoined', models.DateField(default=datetime.datetime(2015, 3, 22, 15, 54, 28, 638864), verbose_name=b'Date Joined the Team')),
                ('dateLeft', models.DateField(default=datetime.datetime(2015, 3, 22, 15, 54, 28, 638883), verbose_name=b'Date Left the Team')),
                ('member', models.ForeignKey(verbose_name=b'Team Member', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(verbose_name=b'Connected Project', to='projects.Project')),
            ],
            options={
                'ordering': ['member'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamMemberSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member', models.ForeignKey(verbose_name=b'Team Member', to='projects.TeamMember')),
                ('project', models.ForeignKey(verbose_name=b'Project', to='projects.Project')),
                ('skill', models.ForeignKey(verbose_name=b'Skill', to='projects.Skill')),
            ],
            options={
                'ordering': ['project'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='projectskill',
            name='skill',
            field=models.ForeignKey(verbose_name=b'Required Skill', to='projects.Skill'),
            preserve_default=True,
        ),
    ]
