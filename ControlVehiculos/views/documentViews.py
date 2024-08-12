from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from django.urls import reverse_lazy
from ..models import Document

class DocumentListView(ListView):
    model = Document
    template_name = 'document/document_list.html'

class DocumentDetailView(DetailView):
    model = Document
    template_name = 'document/document_detail.html'

class DocumentCreateView(CreateView):
    model = Document
    template_name = 'document/document_form.html'
    fields = ['tipo', 'fecha_inicio','fecha_vencimiento','car',]
    success_url = reverse_lazy('document_list')

class DocumentUpdateView(UpdateView):
    model = Document
    template_name = 'document/document_form.html'
    fields = ['tipo', 'fecha_inicio','fecha_vencimiento','car',]
    success_url = reverse_lazy('document_list')

class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'document/document_confirm_delete.html'
    success_url = reverse_lazy('document_list')
