from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from main.models import Category, Technique, Painting, PaintingImage


class PaintingImageInline(admin.TabularInline):
    model = PaintingImage
    extra = 1
    max_num = 10
    fields = ('image', 'preview', 'order')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px;">', obj.image.url)
        return '—'
    preview.short_description = 'Превью'


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Technique)
class TechniqueAdmin(TranslationAdmin):
    list_display = ('name',)


@admin.register(Painting)
class PaintingAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'technique', 'year', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    list_filter = ('category', 'technique', 'is_published')
    search_fields = ('title',)
    inlines = (PaintingImageInline,)
    fields = (
        'title', 'description', 'main_image',
        'category', 'technique', 'year', 'dimensions',
        'is_published', 'order',
    )