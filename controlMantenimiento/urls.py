from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # Rutas para Vehiculo
    path('vehiculos/', views.VehiculoListView.as_view(),name='vehiculo_list'),
    path('vehiculos/<int:pk>/', views.VehiculoDetailView.as_view(), name='vehiculo_detail'),
    path('vehiculos/nuevo/', views.VehiculoCreateView.as_view(), name='vehiculo_create'),
    path('vehiculos/<int:pk>/editar/', views.VehiculoUpdateView.as_view(), name='vehiculo_update'),
    path('vehiculos/<int:pk>/eliminar/', views.VehiculoDeleteView.as_view(), name='vehiculo_delete'),

    # Rutas para TipoMantenimiento
    path('tipos_mantenimiento/', views.TipoMantenimientoListView.as_view(), name='tipo_mantenimiento_list'),
    path('tipos_mantenimiento/<int:pk>/', views.TipoMantenimientoDetailView.as_view(), name='tipo_mantenimiento_detail'),
    path('tipos_mantenimiento/nuevo/', views.TipoMantenimientoCreateView.as_view(), name='tipo_mantenimiento_create'),
    path('tipos_mantenimiento/<int:pk>/editar/', views.TipoMantenimientoUpdateView.as_view(), name='tipo_mantenimiento_update'),
    path('tipos_mantenimiento/<int:pk>/eliminar/', views.TipoMantenimientoDeleteView.as_view(), name='tipo_mantenimiento_delete'),

    # Rutas para Mantenimiento
    path('mantenimientos/', views.MantenimientoListView.as_view(), name='mantenimiento_list'),
    path('mantenimientos/<int:pk>/', views.MantenimientoDetailView.as_view(), name='mantenimiento_detail'),
    path('mantenimientos/nuevo/', views.MantenimientoCreateView.as_view(), name='mantenimiento_create'),
    path('mantenimientos/<int:pk>/editar/', views.MantenimientoUpdateView.as_view(), name='mantenimiento_update'),
    path('mantenimientos/<int:pk>/eliminar/', views.MantenimientoDeleteView.as_view(), name='mantenimiento_delete'),

    # Rutas para Documento
    path('documentos/', views.DocumentoListView.as_view(), name='documento_list'),
    path('documentos/<int:pk>/', views.DocumentoDetailView.as_view(), name='documento_detail'),
    path('documentos/nuevo/', views.DocumentoCreateView.as_view(), name='documento_create'),
    path('documentos/<int:pk>/editar/', views.DocumentoUpdateView.as_view(), name='documento_update'),
    path('documentos/<int:pk>/eliminar/', views.DocumentoDeleteView.as_view(), name='documento_delete'),
    
    # Rutas para Proveedor
    path('provedores/', views.ProveedorListView.as_view(), name='proveedor_list'),
    path('provedores/<int:pk>/', views.ProveedorDetailView.as_view(), name='proveedor_detail'),
    path('provedores/nuevo/', views.ProveedorCreateView.as_view(), name='proveedor_create'),
    path('provedores/<int:pk>/editar/', views.ProveedorUpdateView.as_view(), name='proveedor_update'),
    path('provedores/<int:pk>/eliminar/', views.ProveedorDeleteView.as_view(), name='proveedor_delete'),
]