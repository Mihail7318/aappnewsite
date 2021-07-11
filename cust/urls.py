from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', Setting),

    path('faq/', faq),
    path('privacypolicy/', privacypolicy),
    path('contact/', contact),
    path('aboutus/', aboutus),
    path('useragreement/', useragreement),

]
