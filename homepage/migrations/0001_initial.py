# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=b'static/images/items')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
