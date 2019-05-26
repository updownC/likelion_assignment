"""mini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from fridge import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='login'),
    path('home', views.home, name='home'),
    path('new', views.new, name='new'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
    path('cohome/', views.cohome, name = 'cohome'),
    path('conew/', views.conew, name='conew'),
    path('detail/', views.detail, name="detail2"),
    path('codetail/<int:copost_pk>/', views.codetail, name='codetail'),
    path('coedit/<int:copost_pk>/', views.coedit, name = 'coedit'),
    path('codelete/<int:copost_pk>/', views.codelete, name = 'codelete'),
    path('recipe/', views.recipe, name = 'recipe'), 
    path('detail/<int:post_pk>/', views.detail, name='detail'),
    path('edit/<int:post_pk>/', views.edit, name='edit'),
    path('delete/<int:post_pk>/', views.delete, name='delete'),
    path('about/', views.about, name = 'about'),
    path('new/', views.new, name = 'new'),
]
