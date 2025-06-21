#Gerencia as rotas principais do projeto. Faz o link entre as URLs do projeto e os apps.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vendas_app.urls')),
]
