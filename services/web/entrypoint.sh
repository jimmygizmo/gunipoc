#!/bin/sh

# This script requires nc (netcat) to be installed on the host (container)
# In this case it is a lightweight Python container.

if [ "$DATABASE" = "postgres" ]
then
    echo "[ANY ENV] Web entrypoint script: Waiting for PostgreSQL port to go to LISTEN state ..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "[ANY ENV] Web entrypoint script: PostgreSQL started"
fi


if [ "$FLASK_ENV" = "development" ]
then
    echo "[DEV] Creating the database tables..."
    python manage.py create_db
    echo "[DEV] Tables created"
fi

python manage.py create_db

exec "$@"

