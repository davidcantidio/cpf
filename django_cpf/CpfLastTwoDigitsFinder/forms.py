from .models import Cpf 
from django.forms import ModelForm

class CpfForm(ModelForm):
    class Meta:
        model = Cpf
        fields = '__all__'