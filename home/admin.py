from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

# Register your models here.
from home.models import Standartpages, Partner, Faq, Document

@admin.register(Standartpages)
class StandartpagesAdmin(admin.ModelAdmin):
    save_on_top = True
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    save_on_top = True


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    save_on_top = True


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('id', 'name', 'get_image')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '-'

    get_image.short_description = 'минеатюра'
