#Configuração para rodar o projeto em servidores ASGI (assíncronos).
# Usado em websockets e tempo real.
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjetoDjango.settings')

application = get_asgi_application()
