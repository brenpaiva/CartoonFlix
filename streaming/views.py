from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView #lass based views
from django.contrib.auth.mixins import LoginRequiredMixin


class Homepage(FormView):
    template_name = 'homepage.html'
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: 
            return redirect ('streaming:homefilmes')
        else:
            return super().get(request, *args, **kwargs)


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html' 
    model = Filme #object_list, pega todas lista de filmes do bd


class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    
    def get (self, request, *args, **kwargs): # contabiliza e salva visualização
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        return super().get(request, *args, **kwargs) 

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context


class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None
        

class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('streaming:homefilmes')


class Criarconta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('streaming:login')


class Filmeporcategoria(LoginRequiredMixin, ListView):
    template_name = 'categoria.html' 
    
    def get_queryset(self):
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['filmes_nostalgia'] = Filme.objects.filter(categoria='NOSTALGIA')
        context['filmes_infantil'] = Filme.objects.filter(categoria='INFANTIL')
        context['filmes_classico'] = Filme.objects.filter(categoria='CLASSICO')
        context['filmes_aventura'] = Filme.objects.filter(categoria='AVENTURA')
        return context
