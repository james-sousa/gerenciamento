from django import forms
from website.models import Funcionario


class InsereFuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'sobrenome', 'cpf', 'cargo', 'tempo_de_servico', 'remuneracao']
    

