from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import DraggableMPTTAdmin

from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at',  'views',)
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'views')
    list_editable = ()
    list_filter = ('category',)
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

