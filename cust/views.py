from django.shortcuts import render
from django.http import HttpResponseRedirect

from cust.forms import DocumentForm

from .models import Setting, Standartpages, Faq


def Upload_file(request):
  if request.method == 'POST':
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
  else:
    form =DocumentForm()

  return render(request, 'file_upload.html', {'form': form})



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
    return render(request, 'cust/pages/FAQ.html', context=context )


#privacypolicy
def privacypolicy(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    return render(request, 'cust/pages/privacypolicy.html', context=context )

#aboutus
def aboutus(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    return render(request, 'cust/pages/aboutus.html', context=context )

#useragreement
def useragreement(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    return render(request, 'cust/pages/useragreement.html', context=context )

#contact
def contact(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    return render(request, 'cust/pages/contact.html', context=context )