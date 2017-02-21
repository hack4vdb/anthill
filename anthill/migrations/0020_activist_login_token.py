# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('anthill', '0019_auto_20160820_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='activist',
            name='login_token',
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True),
        ),
    ]
