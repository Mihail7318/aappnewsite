from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

# Register your models here.
from home.models import Slider

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    save_on_top = True


