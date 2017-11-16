# -*- coding: utf-8 -*-

from django.contrib import admin

from kullanicilar.models import Kullanicilar, Statuler


class StatulerAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'maxpuan', 'minpuan')
    ordering = ('baslik',)


class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ('avatar_goster', 'durum', 'adsoyad', 'email', 'cinsiyet', 'statu', 'sehir', 'kayittarihi')
    list_display_links = list_display
    ordering = ('-kayittarihi', 'durum')


    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]


admin.site.register(Statuler, StatulerAdmin)
admin.site.register(Kullanicilar, KullanicilarAdmin)
