from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profsmena, Category
from django.db.models import F


class Home(ListView) :
    model = Profsmena
    template_name = 'profsmen/profsmena.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context


class ProfsmenasByCategory(ListView):
    template_name = 'profsmen/profsmena_category.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Profsmena.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class GetProfsmena(DetailView):
    model = Profsmena
    template_name = 'profsmen/profsmendetails.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        # self.object.refresh_from_db()
        return context