
from django.urls import path
from ..views.documentViews import *

urlpatterns = [
    path('', DocumentListView.as_view(), name='document_list'),
    path('<int:pk>/', DocumentDetailView.as_view(), name='document_detail'),
    path('nuevo/', DocumentCreateView.as_view(), name='document_new'),
    path('<int:pk>/editar/', DocumentUpdateView.as_view(), name='document_edit'),
    path('<int:pk>/borrar/', DocumentDeleteView.as_view(), name='document_delete'),
]
