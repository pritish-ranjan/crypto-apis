#!/bin/bash

DJANGO_SU_NAME="developer"
DJANGO_SU_EMAIL="developer@dev.com"
DJANGO_SU_PASS="admin"

# Starting Django on port 
PORT=$1
echo "Starting Django on port  $PORT"

# Drop existing database
echo "Drop existing database"
rm -f db.sqlite3

# Create database-crypto
echo "Creating database-crypto"
ls -a
chmod +x ./app/init_db/init-db.sh
sh ./app/init_db/init-db.sh

# Run makemigrations
echo "Run makemigrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Create Django superuser
echo "Create superuser"
DJANGO_SUPERUSER_PASSWORD=$DJANGO_SU_PASS python manage.py createsuperuser --username $DJANGO_SU_NAME --email $DJANGO_SU_EMAIL --noinput

# Start server
echo "Starting server on port $PORT"
python manage.py runserver 0.0.0.0:$PORT