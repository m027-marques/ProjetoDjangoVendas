#Criação dos modelos de dados. Cada classe vira uma tabela no banco de dados.
# Importa o módulo models do Django, que permite criar modelos de banco de dados
from django.db import models

# Criação da classe Funcionario, que representa uma tabela no banco de dados
# Cada instância da classe será um registro (uma linha) na tabela Funcionario
class Funcionario(models.Model):

    # Campo de texto para armazenar o nome do funcionário
    # max_length=100 → limita o nome a 100 caracteres
    # verbose_name → é o nome legível que aparece no painel admin
    nome = models.CharField(max_length=100, verbose_name='Nome')

    # Campo numérico do tipo Float para armazenar o total de vendas do funcionário
    # verbose_name → nome amigável que aparece no admin
    vendas = models.FloatField(verbose_name='Total de Vendas')

    # Campo numérico do tipo Float para armazenar a meta que o funcionário deve atingir
    meta = models.FloatField(verbose_name='Meta do Mês')

    # Método especial que define como o Django vai exibir este objeto (Funcionario) no painel admin e em consultas
    def __str__(self):
    # Retorna o nome do funcionário quando o objeto for chamado como texto
        return self.nome