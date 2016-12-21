# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-21 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20161219_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='description',
            field=models.TextField(blank=True, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='photo',
            field=models.URLField(verbose_name='foto'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='website',
            field=models.URLField(blank=True, verbose_name='website'),
        ),
    ]
