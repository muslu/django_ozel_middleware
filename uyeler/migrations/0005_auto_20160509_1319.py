# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 13:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uyeler', '0004_auto_20160509_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uyeler',
            name='BitisTarihi',
            field=models.DateField(default=datetime.datetime(2016, 5, 24, 13, 19, 33, 165155), verbose_name='Biti\u015f Tarihi'),
        ),
        migrations.AlterField(
            model_name='uyeler',
            name='Parola',
            field=models.CharField(default='CVK7HEOE', max_length=15, verbose_name='Parola'),
        ),
    ]