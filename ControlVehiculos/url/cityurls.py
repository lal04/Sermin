
from django.urls import path
from ..views.cityViews import *

urlpatterns = [
    path('', CityListView.as_view(), name='city_list'),
    path('<int:pk>/', CityDetailView.as_view(), name='city_detail'),
    path('nuevo/', CityCreateView.as_view(), name='city_new'),
    path('<int:pk>/editar/', CityUpdateView.as_view(), name='city_edit'),
    path('<int:pk>/borrar/', CityDeleteView.as_view(), name='city_delete'),
]
