# -*- coding: utf-8 -*-
from django.contrib import admin

from uyeler.models import Uyeler


class UyelerAdmin(admin.ModelAdmin):
    list_display            =       ('LogoGoster', 'Aktif', 'Ad', 'SoyAd', 'MailGonderebilir', 'YorumYapabilir', 'KayitLimiti', 'KalanLimit', 'Maili', 'KayitTarihi', 'BitisTarihi')
    list_filter             =       ('Aktif',)
    list_per_page           =       20
    date_hierarchy 			=		'KayitTarihi'
    readonly_fields         =       ['user',]



admin.site.register(Uyeler, UyelerAdmin)

