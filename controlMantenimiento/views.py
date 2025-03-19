from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Count, Sum, Q, Max,OuterRef, Subquery, F
from .forms import MantenimientoForm
from django.contrib import messages
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from .models import (HistorialKilometraje, Vehiculo, TipoMantenimiento,
                     Mantenimiento, Documento, Proveedor)

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import now

import json
from decimal import Decimal


@login_required
def cerrar_sesion(request):
    logout(request)
    
    return redirect('login')

@login_required
def home(request):
    
    # Obtiene el vehículo con más mantenimientos en el mes actual
    vehiculo_mas_mantenimientos = Vehiculo.objects.filter(mantenimiento__fecha_mantenimiento__month=datetime.now().month).annotate(num_mantenimientos=Count('mantenimiento')).order_by('-num_mantenimientos').first()

    # Obtiene el tipo de mantenimiento más recurrente
    tipo_mantenimiento_recurrente = TipoMantenimiento.objects.annotate(num_mantenimientos=Count('mantenimiento')).order_by('-num_mantenimientos').first()

    # Calcula el gasto total en mantenimientos del mes actual
    gasto_total_mes = Mantenimiento.objects.filter(fecha_mantenimiento__month=datetime.now().month).aggregate(total=Sum('costo'))['total']
    
    # Obtiene los documentos que están próximos a expirar en los próximos 30 días
    documentos_proximos = Documento.objects.filter(fecha_expiracion__lte=datetime.now() + timedelta(days=30), estado='Pendiente')
    
    # Obtener el último kilometraje de cada vehículo
    ultimos_kilometrajes = (
        HistorialKilometraje.objects.filter(vehiculo=OuterRef('vehiculo'))
        .values('vehiculo')
        .annotate(ultimo_kilometraje=Max('kilometraje'))
        .values('ultimo_kilometraje')
    )

    # Anotar el kilometraje actual del vehículo en cada mantenimiento
    mantenimientos_cercanos = Mantenimiento.objects.annotate(
        kilometraje_actual=Subquery(ultimos_kilometrajes)
    ).filter(
        #kilometraje_proximo_mantenimiento__gte=F('kilometraje_actual') - 500,
        kilometraje_proximo_mantenimiento__lte=F('kilometraje_actual') + 500,
        estado='Pendiente'
    )
    
    
    
    # Calcular el gasto total de los últimos 6 meses
    gastos_mensuales = []
    for i in range(5, -1, -1):
        mes = now() - timedelta(days=i*30)
        gasto_mes = Mantenimiento.objects.filter(fecha_mantenimiento__year=mes.year, fecha_mantenimiento__month=mes.month).aggregate(total=Sum('costo'))['total'] or 0
        # Convertir Decimal a float
        if isinstance(gasto_mes, Decimal):
            gasto_mes = float(gasto_mes)
        gastos_mensuales.append({'mes': mes.strftime('%B'), 'gasto': gasto_mes})

    # Convertir los datos a JSON
    gastos_mensuales_json = json.dumps(gastos_mensuales)

    # Crea el contexto con los datos obtenidos
    context = {
        'vehiculo_mas_mantenimientos': vehiculo_mas_mantenimientos,
        'tipo_mantenimiento_recurrente': tipo_mantenimiento_recurrente,
        'gasto_total_mes': gasto_total_mes,
        'documentos_proximos': documentos_proximos,
        'gastos_mensuales': gastos_mensuales,
        'gastos_mensuales_json': gastos_mensuales_json,
        'mantenimientos_proximos': mantenimientos_cercanos,
        
    }

    # Renderiza la plantilla 'home.html' con el contexto
    return render(request, 'controlMantenimiento/home.html', context)




# Vistas para Vehiculo
class VehiculoListView(LoginRequiredMixin, ListView):
    model = Vehiculo
    template_name = 'controlMantenimiento/vehiculo_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('buscador', '')
        if query:
            queryset = queryset.filter(
                Q(marca__icontains=query) |
                Q(modelo__icontains=query) |
                Q(numero_placa__icontains=query)
                
            )
        return queryset
    

class VehiculoDetailView(LoginRequiredMixin, DetailView):
    model = Vehiculo
    template_name = 'controlMantenimiento/vehiculo_detail.html'

class VehiculoCreateView(LoginRequiredMixin,CreateView):
    model = Vehiculo
    template_name = 'controlMantenimiento/vehiculo_form.html'
    fields = ['marca', 'modelo', 'anio', 'numero_placa']
    success_url = reverse_lazy('vehiculo_list')
    

class VehiculoUpdateView(LoginRequiredMixin,UpdateView):
    model = Vehiculo
    template_name = 'controlMantenimiento/vehiculo_form.html'
    fields = ['marca', 'modelo', 'anio', 'numero_placa']
    success_url = reverse_lazy('vehiculo_list')
    

class VehiculoDeleteView(LoginRequiredMixin,DeleteView):
    model = Vehiculo
    template_name = 'controlMantenimiento/vehiculo_confirm_delete.html'
    success_url = reverse_lazy('vehiculo_list')
    

# Vistas para TipoMantenimiento
class TipoMantenimientoListView(LoginRequiredMixin, ListView):
    model = TipoMantenimiento
    template_name = 'controlMantenimiento/tipo_mantenimiento_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('buscador', '')
        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query)|
                Q(descripcion__icontains=query)
                )
        return queryset

class TipoMantenimientoDetailView(LoginRequiredMixin,DetailView):
    model = TipoMantenimiento
    template_name = 'controlMantenimiento/tipo_mantenimiento_detail.html'

class TipoMantenimientoCreateView(LoginRequiredMixin,CreateView):
    model = TipoMantenimiento
    template_name = 'controlMantenimiento/tipo_mantenimiento_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tipo_mantenimiento_list')
    
    def form_valid(self, form):
        messages.success(self.request, '¡Mantenimiento creado exitosamente!')
        
        return super().form_valid(form)
    

class TipoMantenimientoUpdateView(LoginRequiredMixin, UpdateView):
    model = TipoMantenimiento
    template_name = 'controlMantenimiento/tipo_mantenimiento_form.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('tipo_mantenimiento_list')  # Añadir success_url
    
    def form_valid(self, form):
        messages.success(self.request, '¡Mantenimiento creado exitosamente!')
        
        return super().form_valid(form)
    
    


class TipoMantenimientoDeleteView(LoginRequiredMixin,DeleteView):
    model = TipoMantenimiento
    template_name = 'controlMantenimiento/tipo_mantenimiento_confirm_delete.html'
    success_url = reverse_lazy('tipo_mantenimiento_list')
    
    

# Vistas para Mantenimiento
class MantenimientoListView(LoginRequiredMixin,ListView):
    model = Mantenimiento
    
    template_name = 'controlMantenimiento/mantenimiento_list.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['form']=MantenimientoForm
        return context
    

class MantenimientoDetailView(LoginRequiredMixin,DetailView):
    model = Mantenimiento
    template_name = 'controlMantenimiento/mantenimiento_detail.html'

class MantenimientoCreateView(LoginRequiredMixin, CreateView):
    model = Mantenimiento
    #form_class = MantenimientoForm
    fields = ['proveedor', 'vehiculo','tipo_mantenimiento', 'fecha_mantenimiento', 'kilometraje', 'costo', 'descripcion']
    template_name = 'controlMantenimiento/mantenimiento_form.html'
    success_url = reverse_lazy('mantenimiento_list')

    
    
    
class MantenimientoUpdateView(LoginRequiredMixin, UpdateView):
    model = Mantenimiento
    fields = '__all__'
    template_name = 'controlMantenimiento/mantenimiento_form.html'
    success_url = reverse_lazy('mantenimiento_list')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['proveedor'].widget.attrs.update({'class': 'form-select'})
        form.fields['vehiculo'].widget.attrs.update({'class': 'form-select'})
        form.fields['tipo_mantenimiento'].widget.attrs.update({'class': 'form-select'})
        form.fields['fecha_mantenimiento'].widget.attrs.update({'class': 'form-control'})
        form.fields['kilometraje'].widget.attrs.update({'class': 'form-control'})
        form.fields['kilometraje_proximo_mantenimiento'].widget.attrs.update({'class': 'form-control'})
        form.fields['costo'].widget.attrs.update({'class': 'form-control'})
        form.fields['estado'].widget.attrs.update({'class': 'form-select'})
        form.fields['descripcion'].widget.attrs.update({'class': 'form-control', 'rows': 4})
        return form

    def form_valid(self, form):
        messages.success(self.request, '¡Mantenimiento actualizado exitosamente!')
        return super().form_valid(form)
    
class MantenimientoDeleteView(LoginRequiredMixin,DeleteView):
    model = Mantenimiento
    template_name = 'controlMantenimiento/mantenimiento_confirm_delete.html'
    success_url = reverse_lazy('mantenimiento_list')
    

# Vistas para Documento
class DocumentoListView(LoginRequiredMixin, ListView):
    model = Documento
    template_name = 'controlMantenimiento/documento_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('buscador', '')
        if query:
            queryset = queryset.filter(
                Q(tipo_documento__icontains=query)|
                Q(usuario__username__icontains=query)|
                Q(vehiculo__marca__icontains=query)
  
            )
        return queryset

class DocumentoDetailView(LoginRequiredMixin, DetailView):
    model = Documento
    template_name = 'controlMantenimiento/documento_detail.html'

class DocumentoCreateView(LoginRequiredMixin, CreateView):
    model = Documento
    template_name = 'controlMantenimiento/documento_form.html'
    fields = [
        'tipo_documento',
        'vehiculo', 
        'usuario',
        'fecha_emision',
        'fecha_expiracion',
        ]
    success_url = reverse_lazy('documento_list')
    
    def get_initial(self):
        initial= super().get_initial()
        
        initial['fecha_expiracion']=now().date()+relativedelta(years=5)
        return initial
    
class DocumentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Documento
    fields = '__all__'
    template_name = 'controlMantenimiento/documento_form.html'
   
    success_url = reverse_lazy('documento_list')
    

class DocumentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Documento
    template_name = 'controlMantenimiento/documento_confirm_delete.html'
    success_url = reverse_lazy('documento_list')
    
    
#vista de proveedor
    
class ProveedorListView(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = 'controlMantenimiento/proveedor_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('buscador', '')
        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query)|
                Q(ruc__icontains=query)
            )
        return queryset

class ProveedorDetailView(LoginRequiredMixin, DetailView):
    model = Proveedor
    template_name = 'controlMantenimiento/proveedor_detail.html'

class ProveedorCreateView(LoginRequiredMixin, CreateView):
    model = Proveedor
    template_name = 'controlMantenimiento/proveedor_form.html'
    fields = '__all__'
    success_url = reverse_lazy('proveedor_list')
    

class ProveedorUpdateView(LoginRequiredMixin, UpdateView):
    model = Proveedor
    fields = '__all__'
    template_name = 'controlMantenimiento/proveedor_form.html'
   
    success_url = reverse_lazy('proveedor_list')
    

class ProveedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Proveedor
    template_name = 'controlMantenimiento/proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor_list')
    
#vista de HistorialKilometraje
    
class HistorialKilometrajeListView(LoginRequiredMixin, ListView):
    model = HistorialKilometraje
    template_name = 'controlMantenimiento/historial_kilometraje_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('buscador', '')
        if query:
            queryset = queryset.filter(
                Q(vehiculo__marca__icontains=query)|
                Q(tipo__icontains=query)
            )
        return queryset

class HistorialKilometrajeDetailView(LoginRequiredMixin, DetailView):
    model = HistorialKilometraje
    template_name = 'controlMantenimiento/historial_kilometraje_detail.html'

class HistorialKilometrajeCreateView(LoginRequiredMixin, CreateView):
    model = HistorialKilometraje
    template_name = 'controlMantenimiento/historial_kilometraje_form.html'
    fields = '__all__'
    success_url = reverse_lazy('kilometraje_list')
    

class HistorialKilometrajeUpdateView(LoginRequiredMixin, UpdateView):
    model = HistorialKilometraje
    fields = '__all__'
    template_name = 'controlMantenimiento/historial_kilometraje_form.html'
   
    success_url = reverse_lazy('kilometraje_list')
    

class HistorialKilometrajeDeleteView(LoginRequiredMixin, DeleteView):
    model = HistorialKilometraje
    template_name = 'controlMantenimiento/historial_kilometraje_confirm_delete.html'
    success_url = reverse_lazy('kilometraje_list')