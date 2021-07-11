from modeltranslation.translator import register, TranslationOptions
from .models import Smena

@register(Smena)
class SmenaTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
