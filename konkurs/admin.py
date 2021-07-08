from django.contrib import admin

from .models import *


@admin.register(Fed)
class FedAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'status', 'views', )
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'views')
    list_editable = ('status',)
    list_filter = ('status',)
    save_as = True
    save_on_top = True

@admin.register(Reg)
class RegAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'status', 'views', )
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'views')
    list_editable = ('status',)
    list_filter = ('status',)
    save_as = True
    save_on_top = True

