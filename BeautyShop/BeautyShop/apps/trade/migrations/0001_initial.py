# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-07 16:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=0, verbose_name='\u5546\u54c1\u6570\u91cf')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355\u5546\u54c1',
                'verbose_name_plural': '\u8ba2\u5355\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sn', models.CharField(max_length=30, unique=True, verbose_name='\u8ba2\u5355\u53f7')),
                ('trade_num', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='\u5546\u54c1\u53f7')),
                ('pay_status', models.CharField(choices=[('success', '\u6210\u529f'), ('cancel', '\u53d6\u6d88'), ('waiting', '\u5f85\u652f\u4ed8')], max_length=10, verbose_name='\u652f\u4ed8\u72b6\u6001')),
                ('post_script', models.CharField(max_length=200, verbose_name='\u8ba2\u5355\u7559\u8a00')),
                ('order_mount', models.FloatField(default=0.0, verbose_name='\u8ba2\u5355\u91d1\u989d')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='\u652f\u4ed8\u65f6\u95f4')),
                ('address', models.CharField(default='', max_length=100, verbose_name='\u6536\u8d27\u5730\u5740')),
                ('signer_name', models.CharField(default='', max_length=20, verbose_name='\u7b7e\u6536\u4eba')),
                ('signer_mobile', models.CharField(max_length=11, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355',
                'verbose_name_plural': '\u8ba2\u5355',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=0, verbose_name='\u8d2d\u4e70\u6570\u91cf')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='\u5546\u54c1')),
            ],
            options={
                'verbose_name': '\u8d2d\u7269\u8f66',
                'verbose_name_plural': '\u8d2d\u7269\u8f66',
            },
        ),
    ]