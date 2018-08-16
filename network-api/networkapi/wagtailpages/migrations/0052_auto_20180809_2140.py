# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-09 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0020_add-verbose-name'),
        ('wagtailpages', '0051_auto_20180809_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='participatepage2',
            name='ctaButtonTitle2',
            field=models.CharField(blank=True, max_length=250, verbose_name='Button Text'),
        ),
        migrations.AddField(
            model_name='participatepage2',
            name='ctaButtonURL2',
            field=models.TextField(blank=True, verbose_name='Button URL'),
        ),
        migrations.AddField(
            model_name='participatepage2',
            name='ctaCommitment2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='participatepage2',
            name='ctaHero2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_hero_participate2', to='wagtailimages.Image', verbose_name='Primary Hero Image'),
        ),
        migrations.AddField(
            model_name='participatepage2',
            name='ctaHeroHeader2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='participatepage2',
            name='ctaHeroSubhead2',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]