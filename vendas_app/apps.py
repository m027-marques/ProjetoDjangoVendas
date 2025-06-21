# Arquivo de configuração interna
# do app. O Django usa para registrar
# o app dentro do projeto.
# Importa a classe AppConfig do Django,
# que é usada para configurar o app dentro do projeto

from django.apps import AppConfig

# Cria uma classe de configuração para o aplicativo
# vendas_app
# O nome da classe geralmente é o nome do app seguido
# de 'Config'
class VendasAppConfig(AppConfig):

    # Define o tipo de campo padrão para as chaves
    # primárias (ID) do banco de dados
    # 'BigAutoField' cria um campo automático do
    # tipo inteiro grande (mais seguro para grandes
    # quantidades de dados)
    default_auto_field = 'django.db.models.BigAutoField'

    # Define o nome do app. Esse nome deve ser
    # exatamente igual ao nome da pasta do app
    # (vendas_app)
    name = 'vendas_app'