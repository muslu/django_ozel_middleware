# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 14:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uyeler', '0007_auto_20160509_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uyeler',
            name='BitisTarihi',
            field=models.DateField(default=datetime.datetime(2016, 5, 24, 14, 27, 17, 736670), verbose_name='Biti\u015f Tarihi'),
        ),
        migrations.AlterField(
            model_name='uyeler',
            name='Parola',
            field=models.CharField(default='H0WM7LP1', max_length=15, verbose_name='Parola'),
        ),
    ]