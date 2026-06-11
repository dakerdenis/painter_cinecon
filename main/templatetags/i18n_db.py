from django import template
from django.utils.translation import get_language
from main.models import Translation

register = template.Library()


@register.simple_tag
def t(key, default=''):
    lang = (get_language() or 'ru')[:2]
    try:
        obj = Translation.objects.get(key=key)
    except Translation.DoesNotExist:
        return default or key
    return obj.get(lang) or default or key