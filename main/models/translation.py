from modeltranslation.translator import register, TranslationOptions
from main.models import Category, Technique, Painting


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Technique)
class TechniqueTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Painting)
class PaintingTranslationOptions(TranslationOptions):
    fields = ('title', 'description')