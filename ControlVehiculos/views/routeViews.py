from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from ..models import Route

class RouteListView(ListView):
    model = Route
    template_name = 'route/route_list.html'

class RouteDetailView(DetailView):
    model = Route
    template_name = 'route/route_detail.html'

class RouteCreateView(CreateView):
    model = Route
    template_name = 'route/route_form.html'
    fields = ['fecha_inicio', 'fecha_fin','car', 'user','kilometraje_inicio', 'kilometraje_fin','ciudad_origen', 'ciudad_destino',]
    success_url = reverse_lazy('route_list')

class RouteUpdateView(UpdateView):
    model = Route
    template_name = 'route/route_form.html'
    fields = ['fecha_inicio', 'fecha_fin','car', 'user','kilometraje_inicio', 'kilometraje_fin','ciudad_origen', 'ciudad_destino',]
    success_url = reverse_lazy('route_list')

class RouteDeleteView(DeleteView):
    model = Route
    template_name = 'route/route_confirm_delete.html'
    success_url = reverse_lazy('route_list')
