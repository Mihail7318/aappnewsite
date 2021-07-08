from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', setting),

    path('ru/faq/', faq),
    path('en/faq/', faqen),
    path('', slider),
    path('ru/privacypolicy/', privacypolicy),
    path('en/privacypolicy/', privacypolicyen),
    path('ru/contact/', contact),
    path('en/contact/', contacten),
    path('ru/aboutus/', aboutus),
    path('en/aboutus/', aboutusen),
    path('ru/useragreement/', useragreement),
    path('en/useragreement/', useragreementen),

]
