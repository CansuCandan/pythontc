# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


cinsiyet_listesi = (('erkek', 'Erkek'), ('kadin', 'Kadın'), ('belirtilmedi', 'Belirtilmedi'))


class Statuler(models.Model):
    baslik          = models.CharField(_('Başlık'), max_length=100, help_text=_(u"En fazla 100 karakter olmalı."))
    maxpuan         = models.PositiveIntegerField(_('Max Puan'), default=1000)
    minpuan         = models.PositiveIntegerField(_('Min Puan'), default=500)


    def __str__(self):
        return '%s' % (self.baslik)


    class Meta:
        verbose_name_plural = _(u'Statüler')
        verbose_name        = _(u'Statu')


class Kullanicilar(models.Model):
    user            = models.ForeignKey(User)
    durum           = models.BooleanField(_('Durum'), default=False)
    adsoyad         = models.CharField(_('Ad Soyad'), max_length=120, help_text=_(u"En fazla 120 karakter olmalı."))
    email           = models.EmailField(max_length=120, unique=True)
    parola          = models.CharField(_('Parola'), max_length=32)
    hakkinda        = models.TextField(_('Hakkında'), blank=True, null=True)
    puan            = models.IntegerField(default=50)
    suannerede      = models.CharField(_('Şu an nerede?'), max_length=255, blank=True, null=True)
    cinsiyet        = models.CharField(_('Cinsiyet'), choices=cinsiyet_listesi, default='belirtilmedi', max_length=10)
    ulke            = models.CharField(_('Ülke'), max_length=100)
    sehir           = models.CharField(_('Şehir'), max_length=120)
    yas             = models.PositiveIntegerField()
    statu           = models.ForeignKey(Statuler, verbose_name=_('Statü'))
    avatar          = models.ImageField(_('Profil Görseli'), blank=True, null=True)
    kayittarihi     = models.DateTimeField(_("Kayıt Tarihi"), auto_now=True)


    def __str__(self):
        return '%s' % (self.adsoyad)


    class Meta:
        verbose_name_plural = _(u'Kullanıcılar')
        verbose_name        = _(u'Kullanıcı')


    def avatar_goster(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.avatar.url))
    avatar_goster.short_description = 'Görsel'
    avatar_goster.allow_tags        = True
