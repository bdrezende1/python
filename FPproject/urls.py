"""FPproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from app.views import home, create, store, painel, dologin, dashboard, logouts, changePassword, form, createp, view, edit, update, delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('create/', create),
    path('store/', store),
    path('painel/', painel),
    path('login/', dologin),
    path('dashboard/', dashboard),
    path('logout/', logouts),
    path('senha/', changePassword),
    path('dashboard/form/', form),
    path('dashboard/create/', createp),
    path('view/<int:pk>/', view),
    path('edit/<int:pk>/', edit),
    path('update/<int:pk>/', update),
    path('delete/<int:pk>/', delete),
]
