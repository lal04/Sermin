from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from ..models import City

class CityListView(ListView):
    model = City
    template_name = 'city/city_list.html'

class CityDetailView(DetailView):
    model = City
    template_name = 'city/city_detail.html'

class CityCreateView(CreateView):
    model = City
    template_name = 'city/city_form.html'
    fields = ['nombre',]
    success_url = reverse_lazy('city_list')

class CityUpdateView(UpdateView):
    model = City
    template_name = 'city/city_form.html'
    fields = ['nombre',]
    success_url = reverse_lazy('city_list')

class CityDeleteView(DeleteView):
    model = City
    template_name = 'city/city_confirm_delete.html'
    success_url = reverse_lazy('city_list')
