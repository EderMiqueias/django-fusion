from django.contrib import admin
from django.utils.html import format_html

from .models import Cargo, Contribuinte, Servico, Feature


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Contribuinte)
class ContribuinteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

    def thumbnail(self, obj):
        return format_html('<img src="{}" style="width: 80px; height: 80px">'.format(obj.imagem.thumbs.url))

    thumbnail.short_description = 'Thumbnail'


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature', 'icone', 'ativo', 'modificado')
