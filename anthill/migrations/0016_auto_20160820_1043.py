# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 10:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anthill', '0015_auto_20160817_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetup',
            old_name='activist',
            new_name='activists',
        ),
    ]
