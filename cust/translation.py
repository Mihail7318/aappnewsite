from modeltranslation.translator import register, TranslationOptions
from .models import Faq, Standartpages

@register(Faq)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('problem', 'reply')

@register(Standartpages)
class TagTranslationOptions(TranslationOptions):
    fields = ('privacypolicy', 'useragreement', 'contact', 'aboutus')
