#!/bin/sh

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create a superuser if one doesn't exist
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='admin').exists() or \
User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" \
| python manage.py shell
# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --clear --noinput
chmod -R 775 /home/app/staticfiles
exec gunicorn --bind 0.0.0.0:8000 core.wsgi:application
# Start the application (optional, if you want to start the server immediately)
echo "Starting server..."
exec "$@"