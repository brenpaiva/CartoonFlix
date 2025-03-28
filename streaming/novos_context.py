# contem as variaveis personalizadas que serão utilizadas nos arquivos html
from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    return {"lista_filmes_recentes": lista_filmes}

def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {"lista_filmes_emalta": lista_filmes}

def filme_destaque(request):
    filmes = Filme.objects.order_by('-data_criacao')
    filme = filmes[0] if filmes.exists() else None
    return {"filme_destaque": filme}

def filme_categorias(request):
    pass
