# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-11 10:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0004_auto_20190510_2307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pictures.Category'),
        ),
    ]
