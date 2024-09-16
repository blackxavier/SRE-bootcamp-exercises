#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    echo "Using SQL_HOST: $POSTGRES_HOST"
    echo "Using SQL_PORT: $POSTGRES_PORT"

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
python manage.py migrate
python manage.py collectstatic --no-input --clear
exec "$@"