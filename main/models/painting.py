from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('Название'), max_length=100)
    slug = models.SlugField(_('Слаг'), max_length=120, unique=True)

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
        ordering = ['name']

    def __str__(self):
        return self.name


class Technique(models.Model):
    name = models.CharField(_('Название'), max_length=100)

    class Meta:
        verbose_name = _('Техника')
        verbose_name_plural = _('Техники')
        ordering = ['name']

    def __str__(self):
        return self.name


class Painting(models.Model):
    title = models.CharField(_('Название работы'), max_length=120)
    description = models.TextField(_('Описание'), blank=True)
    main_image = models.ImageField(_('Главное фото'), upload_to='paintings/')

    category = models.ForeignKey(
        Category, verbose_name=_('Категория'),
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='paintings',
    )
    technique = models.ForeignKey(
        Technique, verbose_name=_('Техника'),
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='paintings',
    )

    year = models.PositiveIntegerField(_('Год'), null=True, blank=True)
    dimensions = models.CharField(_('Размеры'), max_length=100, blank=True)

    is_published = models.BooleanField(_('Опубликовано'), default=True)
    order = models.PositiveIntegerField(_('Порядок'), default=0)
    created_at = models.DateTimeField(_('Создано'), auto_now_add=True)

    class Meta:
        verbose_name = _('Картина')
        verbose_name_plural = _('Картины')
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_work', kwargs={'pk': self.pk})


class PaintingImage(models.Model):
    painting = models.ForeignKey(
        Painting, verbose_name=_('Картина'),
        on_delete=models.CASCADE, related_name='images',
    )
    image = models.ImageField(_('Фото'), upload_to='paintings/gallery/')
    order = models.PositiveIntegerField(_('Порядок'), default=0)

    class Meta:
        verbose_name = _('Доп. фото')
        verbose_name_plural = _('Доп. фото')
        ordering = ['order']

    def __str__(self):
        return f'{self.painting.title} — {self.pk}'