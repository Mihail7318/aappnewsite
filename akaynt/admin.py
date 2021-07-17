from django.contrib import admin

from .models import *


@admin.register(CustomUseris)
class CustomUserisAdmin(admin.ModelAdmin):
    list_display = ('id',)
    save_as = True
    save_on_top = True
'''
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "insurance_companies":
            kwargs["queryset"] = Insurance_companies.objects.filter(autor=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
'''

admin.site.register(Customer)
