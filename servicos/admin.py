from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Servico, Subcategoria, Bairro, Prestador
from django.contrib.auth.models import Group

admin.site.register(Servico)

@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('subcategoria_nome','get_categoria')

    @display(description='Serviço')
    def get_categoria(self,obj):
        return obj.servico.servico_nome


#admin.site.register(Subcategoria)

admin.site.register(Bairro)
admin.site.register(Prestador)

admin.site.unregister(Group)