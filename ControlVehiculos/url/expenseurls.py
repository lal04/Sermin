
from django.urls import path
from ..views.expenseViews import *

urlpatterns = [
    path('', ExpenseListView.as_view(), name='expense_list'),
    path('<int:pk>/', ExpenseDetailView.as_view(), name='expense_detail'),
    path('nuevo/', ExpenseCreateView.as_view(), name='expense_new'),
    path('<int:pk>/editar/', ExpenseUpdateView.as_view(), name='expense_edit'),
    path('<int:pk>/borrar/', ExpenseDeleteView.as_view(), name='expense_delete'),
]
