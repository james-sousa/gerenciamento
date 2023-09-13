from typing import Any, Optional
from django.db import models
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from website.models import Funcionario
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from website.formes import InsereFuncionarioForm

def index(request):
    return render(request, 'index.html')

class IndexTemplateView(TemplateView):
    template_name = 'index.html'    

class FuncionarioListView(ListView):
    template_name = 'lista.html'
    model = Funcionario
    context_object_name = "funcionarios"

class FuncionarioUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'

    def get_object(self, queryset=None):
        funcionario = None
        # Os campos {pk} e {slug} estão presentes em self.kwargs
        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if id is not None:
            # Busca o funcionario apartir do id
            funcionario = Funcionario.objetos.filter(id=id).first()
        elif slug is not None:
            # Pega o campo slug do Model
            campo_slug = self.get_slug_field()
            # Busca o funcionario apartir do slug
            funcionario = Funcionario.objetos.filter(**{campo_slug: slug}).first()
        # Retorna o objeto encontrado
    
        return funcionario
    
    success_url = reverse_lazy('lista_funcionarios')

class FuncionarioDeleteView(DeleteView):
    template_name = 'exclui.html'
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy(
        'lista_funcionarios'
    )

class FuncionarioCreateView(CreateView):
    template_name = 'cadastra-funcionario.html'
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy('lista_funcionarios')
    


