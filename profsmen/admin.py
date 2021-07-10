from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from mptt.admin import DraggableMPTTAdmin
from modeltranslation.admin import TranslationAdmin

from .models import *

class PostAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    content_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Profsmena
        fields = '__all__'


@admin.register(Profsmena)
class ProfsmenaAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'category', 'created_at',  'views',)
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'views')
    list_editable = ()
    list_filter = ('category',)
    save_as = True
    save_on_top = True


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    save_as = True
    save_on_top = True
    list_display = ('id', 'get_photo')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    readonly_fields = ('get_photo',)


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'минеатюра'

