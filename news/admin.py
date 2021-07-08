from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from mptt.admin import DraggableMPTTAdmin

from .models import *

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'status', 'views', )
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'views')
    list_editable = ('status',)
    list_filter = ('status', 'category', 'tags',)
    form = PostAdminForm
    save_as = True
    save_on_top = True


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    save_as = True
    save_on_top = True
    list_display = ('tree_actions', 'indented_title', 'id', 'get_photo')
    mptt_indent_field = "some_node_field"
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('indented_title',)
    search_fields = ('name',)
    readonly_fields = ('get_photo',)


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'минеатюра'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('id', 'name', 'get_image')
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '-'

    get_image.short_description = 'минеатюра'


class SettingAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True