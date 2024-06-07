"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from my_proj import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('baza/', views.index, name='bast_page'),
    path('caption1/', views.caption_1, name='caption_1'),
    path('caption2/', views.caption_2, name='caption_2'),
    path('caption3/', views.caption_3, name='caption_3'),
    path('caption4/', views.caption_4, name='caption_4'),
    path('caption5/', views.caption_5, name='caption_5'),
    path('caption6/', views.caption_6, name='caption_6')
]

