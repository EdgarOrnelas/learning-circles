# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studygroups', '0068_auto_20170303_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilitator',
            name='mailing_list_signup',
            field=models.BooleanField(default=False),
        ),
    ]
