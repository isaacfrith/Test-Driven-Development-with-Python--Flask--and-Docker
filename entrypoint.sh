#!/bin/sh

echo "waiting for postgres"

while ! nc -z api-db 5432; do
    sleep 0.1
done

exho "postgres started"

python manage.py run -h 0.0.0.0

