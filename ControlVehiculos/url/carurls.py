
from django.urls import path
from ..views.carViews import *

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('nuevo/', CarCreateView.as_view(), name='car_new'),
    path('<int:pk>/editar/', CarUpdateView.as_view(), name='car_edit'),
    path('<int:pk>/borrar/', CarDeleteView.as_view(), name='car_delete'),
]
