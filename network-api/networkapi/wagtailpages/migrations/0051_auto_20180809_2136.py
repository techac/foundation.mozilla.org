# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-09 21:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0050_auto_20180809_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participatepage2',
            old_name='commitment',
            new_name='ctaCommitment',
        ),
        migrations.RenameField(
            model_name='participatepage2',
            old_name='primaryHero',
            new_name='ctaHero',
        ),
        migrations.RenameField(
            model_name='participatepage2',
            old_name='heroHeader',
            new_name='ctaHeroHeader',
        ),
        migrations.RenameField(
            model_name='participatepage2',
            old_name='heroSubhead',
            new_name='ctaHeroSubhead',
        ),
    ]