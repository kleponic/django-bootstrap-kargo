# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_auto_20160609_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odvehicle',
            name='photo',
            field=models.ImageField(default='upload/no-img.png', upload_to='upload/'),
        ),
    ]
