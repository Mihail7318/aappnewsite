from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', ProfsmenasByCategory.as_view(), name='category'),
    path('<str:slug>/', GetProfsmena.as_view(), name='post'),
]

