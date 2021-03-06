# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_auto_20160704_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='ml_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tables.ML_Model'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='sp_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tables.SP_Model'),
        ),
    ]
