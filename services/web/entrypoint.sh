#!/bin/sh

# This script requires nc (netcat) to be installed on the host (container)
# In this case it is a lightweight Python container.

if [ "$DATABASE" = "postgres" ]
then
    echo "[DEV] Web entrypoint script: Waiting for PostgreSQL port to go to LISTEN state ..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "[DEV] Web entrypoint script: PostgreSQL started"
fi

python manage.py create_db

exec "$@"

