# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-28 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0006_auto_20180927_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='privacy_policy',
            new_name='privacy_policy_reading_level',
        ),
        migrations.AddField(
            model_name='product',
            name='privacy_policy_url',
            field=models.URLField(blank='True'),
        ),
    ]
