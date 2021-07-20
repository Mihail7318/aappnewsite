from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag
from django.db.models import F
from django.template.defaulttags import register
from .utils import create_comments_tree

@register.filter
def get_all_tag(value):
    return Tag.objects.all()

@register.filter
def get_all_category(value):
    return Category.objects.all()

def get_rubrics_tag(self, context):
    if self.request.LANGUAGE_CODE == "ru":
        context['title_rubrics'] = 'Все рубрики'
    if self.request.LANGUAGE_CODE == "en":
        context['title_rubrics'] = 'All rubrics'

    if self.request.LANGUAGE_CODE == "ru":
        context['title_tag'] = 'Все теги'
    if self.request.LANGUAGE_CODE == "en":
        context['title_tag'] = 'All tag'


class Home(ListView) :
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        get_rubrics_tag(self, context)

        return context


class PostsByCategory(ListView):
    template_name = 'news/news.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.LANGUAGE_CODE == "ru":
            buffer = Category.objects.get(slug=self.kwargs['slug'])
            context['title'] ="Категория " + buffer.name_ru
        if self.request.LANGUAGE_CODE == "en":
            buffer = Category.objects.get(slug=self.kwargs['slug'])
            context['title'] = "Category "+buffer.name_en

        return context



class PostsByTag(ListView):
    template_name = 'news/news.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        buffer = Tag.objects.get(slug=self.kwargs['slug'])
        get_rubrics_tag(self, context)
        if self.request.LANGUAGE_CODE == "ru":
            context['title'] = 'Записи по тегу ' + str(buffer.name_ru)
        if self.request.LANGUAGE_CODE == "en":
            context['title'] = 'Entries by tag ' + str(buffer.name_en)

        return context


class GetPost(DetailView):
    model = Post
    template_name = 'news/newsdetails.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        get_rubrics_tag(self, context)
        self.object.views = F('views') + 1
        self.object.save()
        # self.object.refresh_from_db()
        return context

def base_view(request):
    comments = Post.objects.first().comment.all()
    result = create_comments_tree(comments)
    return render(request, 'news/comments.html', {'comments': result})