# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-31 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20160131_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalitem',
            name='disponible_a_la_vente',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='disponible_a_la_vente',
            field=models.BooleanField(default=True),
        ),
    ]
