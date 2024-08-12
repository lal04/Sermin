from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from ..models import Car

class CarListView(ListView):
    model = Car
    template_name = 'car/car_list.html'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car/car_detail.html'

class CarCreateView(CreateView):
    model = Car
    template_name = 'car/car_form.html'
    fields = ['modelo', 'placa',]
    success_url = reverse_lazy('car_list')

class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car/car_form.html'
    fields = ['modelo', 'placa',]
    success_url = reverse_lazy('car_list')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car/car_confirm_delete.html'
    success_url = reverse_lazy('car_list')
