from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView

from .models import Popsov, Exsov

from django.db.models import F


class HomePop(ListView):
    model = Popsov
    template_name = 'sovet/popsovet.html'
    context_object_name = 'postpops'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context

class GetPostPop(DetailView):
    model = Popsov
    template_name = 'sovet/popdetails.html'
    context_object_name = 'postpop'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        # self.object.refresh_from_db()
        return context


#--------------------------------------------------

class HomeEx(ListView) :
    model = Exsov
    template_name = 'sovet/exsovet.html'
    context_object_name = 'postexs'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context

class GetPostEx(DetailView):
    model = Exsov
    template_name = 'sovet/exdetails.html'
    context_object_name = 'postex'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        # self.object.refresh_from_db()
        return context