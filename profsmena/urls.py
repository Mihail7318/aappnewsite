from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('<str:slug>/', GetSmena.as_view(), name='smena'),


    #path('category/<str:slug>/', get_category, name='category'),
    #path('news/<int:news_id>/', view_news, name='view_news'),

]

