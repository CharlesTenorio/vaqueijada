from django.db import models
from categoria.models import Categoria
from classificacao.models import Classificacao
from vaqueiros.models import Vaqueiro
from eventos.models import Evento
from webvaquejada.settings import RESULTADOS
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from django.core.exceptions import ValidationError


class Corrida(models.Model):
    eventos = models.ForeignKey(Evento, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    senha = models.CharField(max_length=10)
    vaqueiro = models.CharField(max_length=40)
    primeiro_boi = models.CharField(choices=RESULTADOS, max_length=50, blank=True, null=True, default='---',
                                    verbose_name='1° Boi')
    hora_p = models.TimeField(blank=True, null=True, verbose_name='hora')
    segundo_boi = models.CharField(choices=RESULTADOS, max_length=50, blank=True, null=True, default='---',
                                   verbose_name='2° Boi')
    hora_s = models.TimeField(blank=True, null=True, verbose_name='hora')
    terceiro_boi = models.CharField(choices=RESULTADOS, max_length=50, blank=True, null=True, default='---',
                                    verbose_name='3° Boi')
    hora_t = models.TimeField(blank=True, null=True, verbose_name='hora')
    quarto_boi = models.CharField(choices=RESULTADOS, max_length=50, blank=True, null=True, default='---',
                                  verbose_name='4° Boi')
    hora_q = models.TimeField(blank=True, null=True, verbose_name='hora')
    quinto_boi = models.CharField(choices=RESULTADOS, max_length=50, blank=True, null=True, default='---',
                                  verbose_name='5° Boi')
    hora_qt = models.TimeField(blank=True, null=True, verbose_name='hora')

    sexto_boi = models.CharField(choices=RESULTADOS, max_length=50, blank=True, null=True, default='---',
                                 verbose_name='6° Boi')
    hora_sx = models.TimeField(blank=True, null=True, verbose_name='hora')

    setimo_boi = models.CharField(choices=RESULTADOS, max_length=50, blank=True, null=True, default='---',
                                  verbose_name='7° Boi')
    hora_st = models.TimeField(blank=True, null=True, verbose_name='hora')

    oitavo_boi = models.CharField(choices=RESULTADOS, max_length=50, blank=True, null=True, default='---',
                                  verbose_name='8° Boi')
    hora_oitavo = models.TimeField(blank=True, null=True, verbose_name='hora')

    conferida = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.vaqueiro)

    def clean(self):
        if self.vaqueiro == "":
            raise ValidationError("Nome do vaqueiro o brigatório")

        if self.senha == "":
            raise ValidationError("Nome do vaqueiro o brigatório")


class Pontuacao(models.Model):
    corrida = models.ForeignKey(Corrida, on_delete=models.PROTECT)
    eventos = models.ForeignKey(Evento, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    categoria_nome = models.CharField(max_length=80)
    qtd = models.PositiveIntegerField(verbose_name='Total de pontos da categoria')


@receiver(post_save, sender=Corrida)
def update_pontuacao(sender, instance, **kwargs):
    # resul = checa_evento_ativo(instance.eventos_id)
    # if resul:
    criar_pontuacao(instance.eventos_id, instance.categoria_id)
    autalizar_valeu_boi(instance.eventos_id, instance.categoria_id)
    gera_arqvivo()


def autalizar_valeu_boi(id_evento, id_categoria):
    corrida = Corrida.objects.filter(eventos_id=id_evento, categoria_id=id_categoria, conferida=False).all()
    limite_pontuacao = Evento.objects.filter(id=id_evento).first()
    qtd_limit = limite_pontuacao.pontuacao_maxima

    for c in corrida:
        if qtd_limit == 3:
            if c.primeiro_boi == 'Valeu boi' and c.segundo_boi == 'Valeu boi' and c.terceiro_boi == 'Valeu boi':
                qtd_ponto_categoria = pegar_pontos(c.categoria_id)
                qtd_ponto_categoria = qtd_ponto_categoria + 1
                contar_potno(c.categoria_id, qtd_ponto_categoria)
                upd_conferencia_corrida(c.id)

                if not existe_clissificado(c.id):
                    add_classificacao(c.id, c.eventos_id, c.categoria_id, c.senha, c.vaqueiro)

        elif qtd_limit == 4:
            if c.primeiro_boi == 'Valeu boi' and c.segundo_boi == 'Valeu boi' and c.terceiro_boi == 'Valeu boi' and c.quarto_boi == 'Valeu boi':
                qtd_ponto_categoria = pegar_pontos(c.categoria_id)
                qtd_ponto_categoria = qtd_ponto_categoria + 1
                contar_potno(c.categoria_id, qtd_ponto_categoria)
                upd_conferencia_corrida(c.id)

                if not existe_clissificado(c.id):
                    add_classificacao(c.id, c.eventos_id, c.categoria_id, c.senha, c.vaqueiro)

        elif qtd_limit == 5:
            if c.primeiro_boi == 'Valeu boi' and c.segundo_boi == 'Valeu boi' \
                    and c.terceiro_boi == 'Valeu boi' and c.quarto_boi == 'Valeu boi' and c.quinto_boi == 'Valeu boi':
                qtd_ponto_categoria = pegar_pontos(c.categoria_id)
                qtd_ponto_categoria = qtd_ponto_categoria + 1
                contar_potno(c.categoria_id, qtd_ponto_categoria)
                upd_conferencia_corrida(c.id)

                if not existe_clissificado(c.id):
                    add_classificacao(c.id, c.eventos_id, c.categoria_id, c.senha, c.vaqueiro)


        elif qtd_limit == 6:
            if c.primeiro_boi == 'Valeu boi' and c.segundo_boi == 'Valeu boi' \
                    and c.terceiro_boi == 'Valeu boi' and c.quarto_boi == 'Valeu boi' \
                    and c.quinto_boi == 'Valeu boi' and c.sexto_boi == 'Valeu boi':
                qtd_ponto_categoria = pegar_pontos(c.categoria_id)
                qtd_ponto_categoria = qtd_ponto_categoria + 1
                contar_potno(c.categoria_id, qtd_ponto_categoria)
                upd_conferencia_corrida(c.id)

                if not existe_clissificado(c.id):
                    add_classificacao(c.id, c.eventos_id, c.categoria_id, c.senha, c.vaqueiro)


        elif qtd_limit == 7:
            if c.primeiro_boi == 'Valeu boi' and c.segundo_boi == 'Valeu boi' \
                    and c.terceiro_boi == 'Valeu boi' and c.quarto_boi == 'Valeu boi' \
                    and c.quinto_boi == 'Valeu boi' and c.sexto_boi == 'Valeu boi'\
                    and c.setimo_boi == 'Valeu boi':
                qtd_ponto_categoria = pegar_pontos(c.categoria_id)
                qtd_ponto_categoria = qtd_ponto_categoria + 1
                contar_potno(c.categoria_id, qtd_ponto_categoria)
                upd_conferencia_corrida(c.id)
                if not existe_clissificado(c.id):
                    add_classificacao(c.id, c.eventos_id, c.categoria_id, c.senha, c.vaqueiro)


        elif qtd_limit == 8:
            if c.primeiro_boi == 'Valeu boi' and c.segundo_boi == 'Valeu boi' \
                    and c.terceiro_boi == 'Valeu boi' and c.quarto_boi == 'Valeu boi' \
                    and c.quinto_boi == 'Valeu boi' and c.sexto_boi == 'Valeu boi' \
                    and c.setimo_boi == 'Valeu boi' and c.oitavo_boi == 'Valeu boi':
                qtd_ponto_categoria = pegar_pontos(c.categoria_id)
                qtd_ponto_categoria = qtd_ponto_categoria + 1
                contar_potno(c.categoria_id, qtd_ponto_categoria)
                upd_conferencia_corrida(c.id)
                add_classificacao(c.id, c.eventos_id, c.categoria_id, c.senha, c.vaqueiro)

                if not existe_clissificado(c.id):
                    add_classificacao(c.id, c.eventos_id, c.categoria_id, c.senha, c.vaqueiro)


        else:
            break
            print("valor nao valido ")


def criar_pontuacao(id_evento, id_categoria) -> None:
    pt = Pontuacao.objects.filter(eventos_id=id_evento, categoria_id=id_categoria).count()
    if pt > 0:
        print('já existe')
    else:
        corrida = Corrida.objects.filter(eventos_id=id_evento, categoria_id=id_categoria).all()
        for c in corrida:
            p = Pontuacao.objects.create(corrida_id=c.id, eventos_id=c.eventos_id, categoria_id=c.categoria_id,
                                         categoria_nome=c.categoria, qtd=0)
            print('criando a tbl de pontuacao')


def contar_potno(id_categoria, qtd_ponto):
    valeu_boi = Pontuacao.objects.filter(categoria_id=id_categoria).update(qtd=qtd_ponto)


def pegar_pontos(id_categoria):
    result = Pontuacao.objects.select_related('categoria').filter(categoria_id=id_categoria).values(
        'categoria_nome').order_by('id').annotate(qtd_pontos=Sum('qtd'))
    qtd = 0
    for r in result:
        qtd = r["qtd_pontos"]
    return qtd


def pegar_limit_pontuacao(id_vento):
    pt = Evento.objects.filter(id=id_vento).first()
    return pt.pontuacao_maxima


def gera_arqvivo():
    result = Pontuacao.objects.values('categoria_nome').order_by('id').annotate(qtd_pontos=Sum('qtd'))
    for r in result:
        nome_file = r["categoria_nome"]
        qtd = nome_file + ':' + str(r["qtd_pontos"])
        criar_arquivo(nome_file, qtd)


def checa_evento_ativo(id_evento) -> bool:
    ev = Evento.objects.filter(id=id_evento, ativo=True).first()
    if ev.ativo:
        return True
    else:
        return False


def criar_arquivo(nome_arquivo, linha):
    nome = nome_arquivo + '.txt'
    with open(nome, 'w') as qtd_cat:
        qtd_cat.write(f'{linha}\n')


def upd_conferencia_corrida(id_corrida):
    corrida = Corrida.objects.filter(id=id_corrida).update(conferida=True)


def add_classificacao(id_corrida, id_eventos, id_categoria, senha, vaqueiro):
    cl = Classificacao.objects.create(corrida=id_corrida, eventos_id=id_eventos, categoria_id=id_categoria,
                                      senha=senha, vaqueiro=vaqueiro)


def existe_clissificado(id_corrida):
    if Classificacao.objects.filter(corrida=id_corrida).exists():
        return True
    else:
        return False
