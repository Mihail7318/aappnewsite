from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

from .forms import DocumentForm
from django.core.files.storage import FileSystemStorage


from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Setting, Standartpages, Slider, Faq

from aappnewsite import settings

def Upload_file(request):
  if request.method == 'POST':
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
  else:
    form =DocumentForm()

  return render(request, 'file_upload.html', {'form': form})

#slider
def slider(request):
    slider = Slider.objects.all()
    context = {
        'slider': slider,
        'title': 'Главная'
    }
    return render(request, 'home/home.html', context=context )

#setting
def setting(request):
    setting = Setting.objects.all()
    context = {
        'setting': setting,
        'title': 'Главная'
    }
    return render(request, 'base/base.html', context=context )



#Faq
def faq(request):
    faq = Faq.objects.all()
    context = {
        'faq': faq,
    }
    return render(request, 'home/pages/FAQ.html', context=context )

#FaqEN
def faqen(request):
    faq = Faq.objects.all()
    context = {
        'faq': faq,
    }
    return render(request, 'home/pages/FAQen.html', context=context )


#privacypolicy
def privacypolicy(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    return render(request, 'home/pages/privacypolicy.html', context=context )

#privacypolicy-en
def privacypolicyen(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    return render(request, 'home/pages/privacypolicyen.html', context=context )


#aboutus
def aboutus(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    return render(request, 'home/pages/aboutus.html', context=context )

#aboutusEN
def aboutusen(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    return render(request, 'home/pages/aboutusen.html', context=context )


#useragreement
def useragreement(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    return render(request, 'home/pages/useragreement.html', context=context )

#useragreementEN
def useragreementen(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    return render(request, 'home/pages/useragreementen.html', context=context )


#contactru
def contact(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    return render(request, 'home/pages/contact.html', context=context )

#contacten
def contacten(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    return render(request, 'home/pages/contacten.html', context=context )