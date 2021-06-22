"""hackernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# Api
from rest_framework import routers
from app.api.views import NewsViewSet
# Web
from app.web.views import home, add_news

""" Rutas del api """
# establezco la ruta principal para el api
router = routers.DefaultRouter()
# establezco la ruta para mi endpoint
router.register(r'v1/news', NewsViewSet)

""" Rutas de la web """
urlpatterns = [
    path('', home, name='list'),
    path('add-news', add_news, name='add-news'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
