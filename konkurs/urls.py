from django.urls import path

from .views import *

urlpatterns = [
    path('ru/fed/', fed),
    path('ru/reg/', reg),

]
