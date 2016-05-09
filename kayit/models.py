# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Haberler(models.Model):
    user = models.ForeignKey(User)
    Baslik      = models.CharField(u'Başlık', max_length=150)
    KisaIcerik  = models.CharField(u'Kısa içerik', max_length=150)
    Icerik      = models.TextField(u'İçerik')
    Link        = models.SlugField(u'Otomatik Link', max_length=250)
    IslemTarihi = models.DateTimeField(u"İşlem Tarihi", auto_now=True)

    def __unicode__(self):
        return self.Baslik

    class Meta:
        verbose_name_plural = u"Haberler"
        verbose_name        = u"Haber"
