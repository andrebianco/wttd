# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='testema',
            field=models.CharField(max_length=100, null=True),
        ),
    ]