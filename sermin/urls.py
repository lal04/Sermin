"""
URL configuration for sermin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from controlMantenimiento.views import home, cerrar_sesion
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('control-mantenimiento/', include('controlMantenimiento.urls')),
    #####esto es provicional hasta que se inserten mas apps
    #path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('logout/', cerrar_sesion, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Redirige la URL raíz a la vista de login
]

