from django.shortcuts import render
from django.http import HttpResponseRedirect

from news.models import Post
from .models import Slider



#slider
def slider(request):
    slider = Slider.objects.all()
    context = {
        'slider': slider,
        'title': 'Главная'
    }
    return render(request, 'home/home.html', context=context )
