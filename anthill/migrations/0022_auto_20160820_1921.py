# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anthill', '0021_auto_20160820_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailLoginJoinMeetupCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invite_code', models.CharField(max_length=10, unique=True)),
                ('activist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anthill.Activist')),
                ('meetup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anthill.Meetup')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='emailloginjoinmeetupcode',
            unique_together=set([('activist', 'meetup')]),
        ),
    ]