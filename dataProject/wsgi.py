import os
import sys

# Ajouter le chemin du projet
path = '/home/anashamza24/dhtproject' 
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

# Définir les variables d'environnement
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dhtproject.settings')

application = get_wsgi_application()
