#importar modulo admin do Django para gerenciamento
from django.contrib import admin

#Importar o modelo do funcionario o arquivo models.py
from .models import Funcionario

#registrar o funcionario para permitir fazer manipulaçoes
#como visualizar, add, editar, deletar

admin.site.register(Funcionario)

