# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
