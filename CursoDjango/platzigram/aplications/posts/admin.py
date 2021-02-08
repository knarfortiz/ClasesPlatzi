#django
from django.contrib import admin

#models
from aplications.posts.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ panel administrativo post """
    # listado
    list_display = ('pk', 'title', 'photo', 'profile')
    list_display_links = ('pk', 'title', 'profile')
    list_editable = ('photo',)

    # Campos de busqueda
    search_fields = ('title', 'profile')

    # filtros
    list_filter = ('created', 'modified')

    # formulario
    fieldsets = (
            ('Identific', {
                'fields': (
                    ('user', 'profile'),
                ),
            }),
            ('Post', {
                'fields': (
                    ('title',),
                    ('photo',), 
                ),
            }),
            ('Metadata', {
                'fields': (('created', 'modified'),),
            })
    )

    # solo lectura
    readonly_fields = ('created', 'modified')


