from django import forms
from .models import Membro, Diretoria, Faq, Contato

class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = ['nome', 'imagem', 'cargo', 'ordem', 'facebook', 'instagram', 'linkedin']
        widgets = {
            'imagem': forms.ClearableFileInput(),
        }

    imagem = forms.FileField(widget=forms.ClearableFileInput())

class DiretoriaForm(forms.ModelForm):
    class Meta:
        model = Diretoria
        fields = ['nome', 'imagem', 'ordem', 'descricao']
        widgets = {
            'imagem': forms.ClearableFileInput(),
        }

    imagem = forms.FileField(widget=forms.ClearableFileInput())

class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['pergunta', 'resposta', 'ordem']

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'telefone', 'whatsapp', 'ordem']
