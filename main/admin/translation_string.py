from django.contrib import admin
from main.models import Translation


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('key', 'text_ru', 'text_en', 'text_az')
    list_editable = ('text_ru', 'text_en', 'text_az')
    search_fields = ('key', 'text_ru', 'text_en', 'text_az')
    list_display_links = ('key',)