# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-11 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0005_auto_20190511_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pictures.Location'),
        ),
    ]
