# -*- coding: utf-8 -*-

from django.contrib import admin

from blog.models import Kategoriler, Makaleler


class KategorilerAdmin(admin.ModelAdmin):
    list_display = ('baslik',)
    prepopulated_fields = {"slug": ("baslik",)}
    ordering = ('baslik',)


class MakalelerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("baslik",)}
    list_display = ('durum', 'kategoriler', 'okumasuresi', 'yazar', 'baslik', 'kayittarihi')
    list_display_links = list_display
    ordering = ('-kayittarihi', 'durum')


    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'yazar':
            kwargs['initial'] = request.user.id
        return super(MakalelerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Kategoriler, KategorilerAdmin)
admin.site.register(Makaleler, MakalelerAdmin)
