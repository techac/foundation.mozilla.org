# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-14 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_auto_20170313_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]