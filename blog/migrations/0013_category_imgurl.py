# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='imgurl',
            field=models.CharField(blank=True, max_length=200, verbose_name='分类图片'),
        ),
    ]