
from django.urls import path
from ..views.routeViews import *

urlpatterns = [
    path('', RouteListView.as_view(), name='route_list'),
    path('<int:pk>/', RouteDetailView.as_view(), name='route_detail'),
    path('nuevo/', RouteCreateView.as_view(), name='route_new'),
    path('<int:pk>/editar/', RouteUpdateView.as_view(), name='route_edit'),
    path('<int:pk>/borrar/', RouteDeleteView.as_view(), name='route_delete'),
]
