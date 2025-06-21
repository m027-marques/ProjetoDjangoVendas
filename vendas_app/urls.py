from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('salvar/', views.salvar, name='salvar'),
    path('analisar/<int:funcionario_id>/', views.analisar, name='analisar'),
    path('historico/', views.historico, name='historico'),
]

