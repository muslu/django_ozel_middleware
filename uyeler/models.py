# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import string
import sys
from datetime import timedelta

from django.contrib.auth.models import User, Group
from django.db import models
from django.utils import timezone



reload(sys)
sys.setdefaultencoding('utf-8')


class Uyeler(models.Model):
    user                = models.ForeignKey(User)
    group               = models.ForeignKey(Group, default=1)
    Aktif               = models.BooleanField(default=1)
    MailGonderebilir    = models.BooleanField(u"Mail Gönderebilir", default=0)
    YorumYapabilir      = models.BooleanField(u"Yorum Yapabilir", default=1)
    KayitLimiti         = models.IntegerField(u"Kayıt Limiti", default=1000)
    Ad                  = models.CharField(u"Adı", max_length=100)
    SoyAd               = models.CharField(u"Soyadı", max_length=100)
    Domain              = models.CharField(u'Domain', default="http://www.", max_length=250, blank=False, null=False, unique=True)
    Parola              = models.CharField(u'Parola',
                              default=''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(8)),
                              max_length=15, blank=False, null=False)

    Maili               = models.EmailField(u'Mail Adresi', max_length=250, blank=False, null=False, unique=True)
    Logo                = models.FileField(u'Logo', upload_to="profilfoto/", max_length=250, blank=True, null=True,
                            help_text="Görsel yüksekliği 200px, genişliği 200px olarak gösterilecek.")

    KayitTarihi = models.DateField(u"Kayıt Tarihi", default=timezone.now)
    BitisTarihi = models.DateField(u"Bitiş Tarihi", default=timezone.now() + timedelta(days=15))

    def __unicode__(self):
        return "%s %s" % (self.Ad, self.SoyAd)

    class Meta:
        verbose_name_plural = u"Üyeler"
        verbose_name = u"Üye"

    def LogoGoster(self):
        return '<center><img src="/static/%s" style="height:200px; width:200px;" /></center>' % self.Logo

    LogoGoster.short_description = u'Profil Foto'
    LogoGoster.allow_tags = True

    def save(self):
        from django.contrib.auth.models import Group

        if self.pk is None:
            user            = User.objects.create_user(username=self.Maili, password=self.Parola, email=self.Maili)
            user.is_staff   = True
            user.first_name = self.Ad.strip()
            user.last_name  = self.SoyAd.strip()
            user.save()

            self.user       = user

            # g = Group.objects.get(name=u'Normal Üye')
            # g.user_set.add(user)

        super(Uyeler, self).save()


    def KalanLimit(self):
        from kayit.models import Haberler
        KullanilanLimit     =  Haberler.objects.filter(user = self.user).count()
        return self.KayitLimiti - KullanilanLimit

    KalanLimit.short_description = u'Kalan Limit'
    KalanLimit.allow_tags = True
