from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [

    path('pop/', HomePop.as_view(), name='homepop'),
    path('pop/<str:slug>/', GetPostPop.as_view(), name='postpop'),
    path('ex/', HomeEx.as_view(), name='homeex'),
    path('ex/<str:slug>/', GetPostEx.as_view(), name='postex'),

]
