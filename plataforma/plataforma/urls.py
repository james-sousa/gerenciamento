"""
URL configuration for plataforma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website import views
urlpatterns = [
    path('',views.IndexTemplateView.as_view(), name='index'),
    path('funcionarios/', views.FuncionarioListView.as_view(), name='lista_funcionarios'),
    path('funcionario/atualiza/<pk>',views.FuncionarioUpdateView.as_view(),name='atualiza_funcionario'),
    path('funcionario/excluir/<pk>', views.FuncionarioDeleteView.as_view(),name='deleta_funcionario'),
    path('funcionario/cadastrar/',views.FuncionarioCreateView.as_view(), name='cadastra_funcionario'),
    path('admin/', admin.site.urls),
]
