from modeltranslation.translator import register, TranslationOptions
from .models import Category, Post, Tag

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
