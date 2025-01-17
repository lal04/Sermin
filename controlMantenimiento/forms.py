from django import forms
from .models import Mantenimiento, Documento

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['proveedor', 'vehiculo', 'tipo_mantenimiento', 'fecha_mantenimiento', 'kilometraje' , 'costo','descripcion']
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-select'}),
            'vehiculo': forms.Select(attrs={'class': 'form-select'}),
            'tipo_mantenimiento': forms.Select(attrs={'class': 'form-select'}),
            'fecha_mantenimiento': forms.DateInput(attrs={'class': 'form-control',}),
            'kilometraje': forms.TextInput(attrs={'class': 'form-control',}),
            'costo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

        
class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'
        widgets = {
            'fecha_emision': forms.DateInput(attrs={'type': 'date'}),
            'fecha_expiracion': forms.DateInput(attrs={'type': 'date'}),
        }
