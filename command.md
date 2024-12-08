# Generate secret key

# Run
"./manage.py shell" or "python manage.py shell"
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())


gunicorn --workers 3 --bind 0.0.0.0:8000 server.wsgi:application --env DJANGO_SETTINGS production
gunicorn server.wsgi:application

gunicorn server.wsgi:application --workers 3 --bind 0.0.0.0:8000