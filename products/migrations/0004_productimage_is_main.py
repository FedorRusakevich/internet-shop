# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-02-13 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190212_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
