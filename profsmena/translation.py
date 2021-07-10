from modeltranslation.translator import register, TranslationOptions
from .models import Category, Smena

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Smena)
class SmenaTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
