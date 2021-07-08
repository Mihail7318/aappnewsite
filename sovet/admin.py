from django.contrib import admin

# Register your models here.
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

# Register your models here.
from sovet.models import Popsov, Exsov

@admin.register(Popsov)
class PopsovAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'created_at', 'status', 'views', )
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'views')
    list_editable = ('status',)
    list_filter = ('status',)
    save_as = True
    save_on_top = True

@admin.register(Exsov)
class ExsovAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'created_at', 'status', 'views', )
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'views')
    list_editable = ('status',)
    list_filter = ('status',)
    save_as = True
    save_on_top = True