from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.db.models import F


class Home(ListView) :
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context

class GetPost(DetailView):
    model = Post
    template_name = 'news/newsdetails.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        # self.object.refresh_from_db()
        return context