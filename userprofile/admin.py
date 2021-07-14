from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, CustomUser, CustomUseris
from userprofile.forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserisCreationForm, CustomUserisChangeForm

class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline,)
    mptt_indent_field = "some_node_field"




@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    exclude = ['region']
    list_display = ['email', 'username',]
    list_display_links = ('username',)

@admin.register(CustomUseris)
class CustomUserisAdmin(UserAdmin):
    add_form = CustomUserisCreationForm
    form = CustomUserisChangeForm
    model = CustomUseris
    exclude = ['parent']
    list_display = ['email', 'username', 'first_name']
    list_display_links = ('username',)

# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)