# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from kullanicilar.models import Kullanicilar


class Kategoriler(models.Model):
    yonetici = models.ForeignKey(Kullanicilar)
    baslik = models.CharField(_('Başlık'), max_length=120, unique=True, help_text=_(u"En fazla 120 karakter olmalı."))
    slug = models.CharField(_('Otomatik Link'), max_length=71, unique=True, help_text=_(u"En fazla 71 karakter olmalı."))


    def __str__(self):
        return '%s' % (self.baslik)


    class Meta:
        verbose_name_plural = _(u'Kategoriler')
        verbose_name = _(u'Kategori')


class Makaleler(models.Model):
    durum = models.BooleanField(_(u'Durum'), default=True)
    kategori = models.ManyToManyField(Kategoriler, verbose_name=_(u'Kategori'))
    yazar = models.ForeignKey(Kullanicilar, verbose_name=_(u'Yazar'))
    baslik = models.CharField(_(u'Başlık'), max_length=71, unique=True, help_text=_(u"En fazla 71 karakter olmalı."))
    aciklama = models.CharField(_(u'Açıklama'), max_length=100, unique=True, help_text=_(u"En fazla 100 karakter olmalı."))
    okumasuresi = models.IntegerField(_(u'Okuma süresi'), help_text=_(u"Yaklaşık okuma süresi"), default=2)
    icerik = models.TextField(_(u'İçerik'), help_text=_(u"En az 3 paragraf halinde yazılmalı."))
    paylasimaj = models.FileField(_(u'Paylaşımda Görsel'), upload_to="paylasimaj/", blank=True, null=True)
    kayittarihi = models.DateTimeField(_(u'Kayıt Tarihi'), auto_now=True)
    slug = models.SlugField(_(u'Link'), max_length=71, help_text=_(u"Otomatik oluşturulacak"))


    def __str__(self):
        return '%s - %s' % (self.yazar.adsoyad, self.baslik)


    class Meta:
        verbose_name_plural = _(u'Makaleler')
        verbose_name = _(u'Makale')


    def kategoriler(self):
        return "<br/>".join([b.baslik for b in self.kategori.all()])


    kategoriler.allow_tags = True
    kategoriler.short_description = 'Kategoriler'
