
from django.urls import path
from ..views.maintenanceViews import *

urlpatterns = [
    path('', MaintenanceListView.as_view(), name='maintenance_list'),
    path('<int:pk>/', MaintenanceDetailView.as_view(), name='maintenance_detail'),
    path('nuevo/', MaintenanceCreateView.as_view(), name='maintenance_new'),
    path('<int:pk>/editar/', MaintenanceUpdateView.as_view(), name='maintenance_edit'),
    path('<int:pk>/borrar/', MaintenanceDeleteView.as_view(), name='maintenance_delete'),
]
