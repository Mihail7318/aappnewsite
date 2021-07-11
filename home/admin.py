from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from news.models import *

# Register your models here.
from .models import *

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'titles', 'created_at', )
    list_display_links = ('id', 'titles')
    list_display_links = ('id', 'titles')
    search_fields = ('titles', 'views')

    save_as = True
    save_on_top = True


