from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, CustomUser
from userprofile.forms import CustomUserCreationForm, CustomUserChangeForm

class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline,)




class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]
    list_display_links = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)