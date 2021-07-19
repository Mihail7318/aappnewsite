from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='glavnaya'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('news/<str:slug>/', GetPost.as_view(), name='post'),

    #path('category/<str:slug>/', get_category, name='category'),
    #path('news/<int:news_id>/', view_news, name='view_news'),

]

