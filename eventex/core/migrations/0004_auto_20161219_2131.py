# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-19 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20161219_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]