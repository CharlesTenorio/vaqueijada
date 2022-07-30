from django.contrib import admin
from .models import Classificacao

class ClassificacaoAdmin(admin.ModelAdmin):
    model = Classificacao
    list_display = ['categoria', 'eventos', 'senha', 'vaqueiro']
    list_filter = ('categoria',)

admin.site.register(Classificacao, ClassificacaoAdmin)