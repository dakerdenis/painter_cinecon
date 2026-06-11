from django.db import models
from django.utils.translation import gettext_lazy as _


class Translation(models.Model):
    key = models.CharField(_('Ключ'), max_length=150, unique=True)
    text_ru = models.CharField(_('Русский'), max_length=500, blank=True)
    text_en = models.CharField(_('English'), max_length=500, blank=True)
    text_az = models.CharField(_('Azərbaycan'), max_length=500, blank=True)

    class Meta:
        verbose_name = _('Перевод интерфейса')
        verbose_name_plural = _('Переводы интерфейса')
        ordering = ['key']

    def __str__(self):
        return self.key

    def get(self, lang):
        return getattr(self, f'text_{lang}', '') or self.text_ru