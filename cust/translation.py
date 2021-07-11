from modeltranslation.translator import register, TranslationOptions
from .models import Faq, Standartpages

@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('problem', 'reply')

@register(Standartpages)
class StandartpagesTranslationOptions(TranslationOptions):
    fields = ('privacypolicy', 'useragreement', 'contact', 'aboutus')
