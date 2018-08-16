# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-08 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0045_auto_20180808_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='participatepage2',
            name='foo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wagtailpages.Foo'),
        ),
    ]