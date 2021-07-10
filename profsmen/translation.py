from modeltranslation.translator import register, TranslationOptions
from .models import Category, Profsmena

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Profsmena)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
