# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 13:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uyeler', '0003_auto_20160509_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uyeler',
            name='BitisTarihi',
            field=models.DateField(default=datetime.datetime(2016, 5, 24, 13, 16, 51, 644440), verbose_name='Biti\u015f Tarihi'),
        ),
        migrations.AlterField(
            model_name='uyeler',
            name='Parola',
            field=models.CharField(default='3OUDFHIX', max_length=15, verbose_name='Parola'),
        ),
    ]
