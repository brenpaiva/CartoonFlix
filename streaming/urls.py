from django.urls import path, include, reverse_lazy
from .views import Homepage, Homefilmes, Detalhesfilme, Pesquisafilme, Paginaperfil, Criarconta, Filmeporcategoria
from django.contrib.auth import views as auth_view




app_name='streaming'

urlpatterns = [  
    path('', Homepage.as_view(), name="homepage"),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name="detalhesfilme"), #URL dinamica de acordo com o id do filme
    path('pesquisa/', Pesquisafilme.as_view(), name ="pesquisafilme"),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy('streaming:homefilmes')), name='mudarsenha'),
    path('categorias/', Filmeporcategoria.as_view(),name='categoria')
    ]
 