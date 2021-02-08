# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from aplications.users.models import Profile
from django.contrib.auth.models import User


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Panel administrativo de perfiles de usuario."""
    # listas 
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')

    # Campos en los cuales realiza busquedas
    search_fields = ('user__email', 'phone_number')

    # Crea panel de filtros
    list_filter = ('created', 'modified')

    # formularios
    fieldsets = (
            ('Profile', {
                'fields': (
                    ('user', 'picture'),
                    # ('phone_number', 'website'),
                ),
            }),
            ('Extra info', {
                'fields': (
                    ('website', 'phone_number'),
                    ('biography'),
                )
            }),
            ('Metadats', {
                'fields': (('created','modified'),),
            })
    )
    # que sean de solo lectura
    readonly_fields = ('created', 'modified')


class ProfileInline(admin.StackedInline):
    """ Extender el modelo de usuario """
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """ Add el modelo de usuario al perfil """
    inlines = (ProfileInline,)
    list_display = (
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
    )

# Se registra el modelo
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

