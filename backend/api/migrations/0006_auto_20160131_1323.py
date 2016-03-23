# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-31 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160101_2325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorie',
            options={},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['categorie', 'nom'], 'verbose_name': 'item', 'verbose_name_plural': 'inventaire'},
        ),
        migrations.AddField(
            model_name='historicalitem',
            name='disponible_a_la_vente',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='disponible_a_la_vente',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
