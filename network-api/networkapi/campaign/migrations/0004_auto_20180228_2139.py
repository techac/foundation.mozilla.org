# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0003_auto_20180206_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='share_email',
            field=models.CharField(blank=True, help_text='Share Progress id for email button', max_length=20),
        ),
        migrations.AddField(
            model_name='petition',
            name='share_facebook',
            field=models.CharField(blank=True, help_text='Share Progress id for facebook button', max_length=20),
        ),
        migrations.AddField(
            model_name='petition',
            name='share_twitter',
            field=models.CharField(blank=True, help_text='Share Progress id for twitter button', max_length=20),
        ),
        migrations.AlterField(
            model_name='petition',
            name='share_link',
            field=models.URLField(blank=True, editable=False, help_text='Link that will be put in share button', max_length=1024),
        ),
        migrations.AlterField(
            model_name='petition',
            name='share_link_text',
            field=models.CharField(blank=True, default='Share this', editable=False, help_text='Text content of the share button', max_length=20),
        ),
    ]