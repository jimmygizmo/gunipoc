#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "[PROD] Web entrypoint script: Waiting for PostgreSQL port to go to LISTEN state ..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "[PROD] Web entrypoint script: PostgreSQL started"
fi

exec "$@"

