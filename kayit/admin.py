from django.contrib import admin

from kayit.models import Haberler


class HaberlerAdmin(admin.ModelAdmin):
    list_display            =       [ 'Baslik', 'IslemTarihi']
    ordering                =       ['-IslemTarihi', ]
    actions_on_bottom       =       True
    actions_on_top          =       True
    list_per_page           =       100
    date_hierarchy          =       'IslemTarihi'
    prepopulated_fields     =       {'Link': ('Baslik', 'KisaIcerik') }



admin.site.register(Haberler, HaberlerAdmin)