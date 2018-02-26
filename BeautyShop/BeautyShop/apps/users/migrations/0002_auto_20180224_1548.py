# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-24 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '\u7537'), ('male', '\u7537')], default='female', max_length=6, verbose_name='\u6027\u522b'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='\u7535\u8bdd'),
        ),
    ]