# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-02-12 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190212_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=24, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Доставка',
                'verbose_name_plural': 'Доставка',
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Delivery'),
        ),
    ]