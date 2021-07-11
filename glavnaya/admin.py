from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from news.models import *

# Register your models here.
from .models import *

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', )
    list_display_links = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'views')

    save_as = True
    save_on_top = True

@admin.register(Vidjet)
class VidjetAdmin(admin.ModelAdmin):
    save_on_top = True
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    save_on_top = True
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True