from django.urls import path
from . import views
from .views import itens, adicionar_inventario

urlpatterns = [
        path('', views.homepage, name="homepage"),         # Inclui as urls do app blog
        path('homepageDark', views.homepageDark, name="homepageDark"),   # Inclui as urls do app blog
        path('login', views.login, name="login"),           # Inclui as urls do app blog

        # URL para processar o cadastro do usuário
        path('cadastroUsuario', views.cadastroUsuario, name='cadastroUsuario'),
        path('profile', views.profile, name="profile"),       # Inclui as urls do app blog
        path('faq', views.faq, name="faq"),                 # Inclui as urls do app blog
        path('welcomeHomepage', views.welcomeHomepage, name="welcomeHomepage"),   # Inclui as urls do app blog
        path('itens', views.itens, name="itens"),           # Inclui as urls do app blog

        # URL para adicionar os patrimônios no banco de dados
        path('itens/', itens, name='itens'),
    path('adicionar-inventario/', adicionar_inventario, name='adicionar_inventario'),
]