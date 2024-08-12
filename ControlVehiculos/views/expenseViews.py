from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from ..models import Expense

class ExpenseListView(ListView):
    model = Expense
    template_name = 'expense/expense_list.html'

class ExpenseDetailView(DetailView):
    model = Expense
    template_name = 'expense/expense_detail.html'

class ExpenseCreateView(CreateView):
    model = Expense
    template_name = 'expense/expense_form.html'
    fields = ['titulo', 'route','descripcion','monto',]
    success_url = reverse_lazy('expense_list')

class ExpenseUpdateView(UpdateView):
    model = Expense
    template_name = 'expense/expense_form.html'
    fields = ['titulo', 'route','descripcion','monto',]
    success_url = reverse_lazy('expense_list')

class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'expense/expense_confirm_delete.html'
    success_url = reverse_lazy('expense_list')
