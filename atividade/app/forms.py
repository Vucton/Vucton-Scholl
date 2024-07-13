from django.forms import ModelForm #Repare na estrutura
from .models import Pessoa

class PessoaForm(ModelForm): #Herdando da classe form do django
    class Meta():
        model = Pessoa
        fields = '__all__'