from django.contrib import admin
from .models import Corrida, Pontuacao
from eventos.models import Evento


@admin.action(description="Atualizar Desclassificado")
def vaquerio_desclassificado(modeladmin, request, queryset):
    for cr in queryset:
        discontar_pontos(cr.categoria_id)



class CorridaAdmin(admin.ModelAdmin):
    search_fields = ["senha", "vaqueiro"]
    actions = [vaquerio_desclassificado, ]
    model = Corrida
    list_display = ['id', 'vaqueiro', 'senha', 'categoria', 'eventos']


class CorridaTabular(admin.TabularInline):
    model = Corrida


class EventoAdmin(admin.ModelAdmin):
    inlines = [CorridaTabular]
    list_display = ["evento", "numero", "dia_semana", "ativo", "data_evento"]
    list_filter = ["dia_semana", "evento"]

    class Meta:
        model = Evento


class PontuacaoAdmin(admin.ModelAdmin):
    model = Pontuacao
    list_display = ['id', 'eventos', 'categoria', 'qtd']
    list_filter = ['eventos', 'categoria']


admin.site.register(Evento, EventoAdmin)
admin.site.register(Corrida, CorridaAdmin)
admin.site.register(Pontuacao, PontuacaoAdmin)


def discontar_pontos(id_categoria):
    cat_ponto = Pontuacao.objects.filter(categoria_id=id_categoria).first()
    pontos_atual = cat_ponto.qtd
    if pontos_atual >= 1:
        pontos_atual = pontos_atual - 1
        upd_ponto = Pontuacao.objects.filter(categoria_id=id_categoria).update(qtd=pontos_atual)
