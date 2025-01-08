from django import forms
from .models import Mantenimiento, Documento

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
        widgets = {
            'fecha_mantenimiento': forms.DateInput(attrs={'type': 'date'}),
            'fecha_proximo_mantenimiento': forms.DateInput(attrs={'type': 'date'}),
        }
        
        
class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'
        widgets = {
            'fecha_emision': forms.DateInput(attrs={'type': 'date'}),
            'fecha_expiracion': forms.DateInput(attrs={'type': 'date'}),
        }
