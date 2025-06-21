#Configuração para rodar o projeto em servidores WSGI (tradicional).
#Usado na maioria dos servidores web.
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjetoDjango.settings')

application = get_wsgi_application()
