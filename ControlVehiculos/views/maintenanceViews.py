from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from django.urls import reverse_lazy
from ..models import Maintenance

class MaintenanceListView(ListView):
    model = Maintenance
    template_name = 'maintenance/maintenance_list.html'

class MaintenanceDetailView(DetailView):
    model = Maintenance
    template_name = 'maintenance/maintenance_detail.html'

class MaintenanceCreateView(CreateView):
    model = Maintenance
    template_name = 'maintenance/maintenance_form.html'
    fields = ['titulo', 'car','fecha_mantenimiento','kilometraje','monto']
    success_url = reverse_lazy('maintenance_list')

class MaintenanceUpdateView(UpdateView):
    model = Maintenance
    template_name = 'maintenance/maintenance_form.html'
    fields = ['titulo', 'car','fecha_mantenimiento','kilometraje','monto']
    success_url = reverse_lazy('maintenance_list')

class MaintenanceDeleteView(DeleteView):
    model = Maintenance
    template_name = 'maintenance/maintenance_confirm_delete.html'
    success_url = reverse_lazy('maintenance_list')
