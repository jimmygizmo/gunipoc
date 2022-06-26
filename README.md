# gunipoc
Proof of concept as part of my switch to using Gunicorn with Flask + NGINX, all in separate containers. I think Gunicorn will be much simpler to use than UWSGI and will likely suit my needs much better and still scale well enough for me.

This proof of concept is being done by following the below tutorial, which I may deviate a little:

Dockerizing Flask with Postgres, Gunicorn, and Nginx
https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/

Gunicorn:
https://gunicorn.org/

-----------------------------
One difference is I am using Pyenv and I created a .python-version file.
The VE is based off 3.10.4. I upgraded pip and setuptools in the VE as usual.
VE name follows my standard: ve.gunipoc

Tutorial steps:
$ mkdir flask-on-docker && cd flask-on-docker
$ mkdir services && cd services
$ mkdir web && cd web
$ mkdir project

$ pip install flask==1.1.2

-------------------------
python manage.py run

I hit an error - could not import name 'escape' from jinja2, within the core
modules jinja2 I think. So I will upgrade Flask, even since this tut uses
an older version. Admittedly, the error does not make me think this will be
the fix, but its work doing anyhow.
New version (upgraded from 1.1.2):
flask-2.1.2

Oh! It turns out this is in fact the correct fix. Per:
https://stackoverflow.com/questions/71718167/importerror-cannot-import-name-escape-from-jinja2

And yes the Flask server comes up:

Running on http://127.0.0.1:5000

http://localhost:5000/

-----------------------------------

For the Python Docker image I will use 3.9.13 instead of 3.9.5.
Note that our VE is currently derived from 3.10.4 and this high version
did cause us to HAVE to upgrade Flask, so sometimes there are issues from
going for the latest versions, but it is still the best strategy.

------------------------------------

I added this step to the Dockerfile, since if they are upgrading pip, well
I usually do both pip and setuptools.

RUN pip install --upgrade setuptools

--------------------------

The flask app comes up fine under docker compose. Now turning to Postgres,
the tutorial specifies the image: postgres:13-alpine
Later I might try a newer postgres image, after I get 13-alpine working:

postgres:14.4-bullseye

-----------------------------------

I increased the version of psycopg2-binary from 2.8.6 to 2.9.3.

The Flask-SQLAlchemy version has no upgrades available yet. It is the latest.

------------------------------------

Everything looks good, in-line with the tutorial so far:
(ve.gunipoc) ➜  web git:(main) ✗ docker volume inspect flask-on-docker_postgres_data

[
{
"CreatedAt": "2022-06-23T12:57:02Z",
"Driver": "local",
"Labels": {
"com.docker.compose.project": "flask-on-docker",
"com.docker.compose.version": "2.6.0",
"com.docker.compose.volume": "postgres_data"
},
"Mountpoint": "/var/lib/docker/volumes/flask-on-docker_postgres_data/_data",
"Name": "flask-on-docker_postgres_data",
"Options": null,
"Scope": "local"
}
]
(ve.gunipoc) ➜  web git:(main) ✗

---------------------------------------

docker-compose exec db psql --username=hello_flask --dbname=hello_flask_dev

hello_flask_dev=# \c hello_flask_devv
FATAL:  database "hello_flask_devv" does not exist
Previous connection kept
hello_flask_dev=# \c hello_flask_dev
You are now connected to database "hello_flask_dev" as user "hello_flask".
hello_flask_dev=# \z
Access privileges
Schema |     Name     |   Type   | Access privileges | Column privileges | Policies
--------+--------------+----------+-------------------+-------------------+----------
public | users        | table    |                   |                   |
public | users_id_seq | sequence |                   |                   |
(2 rows)

hello_flask_dev=#

------------------------------------------------

SKIPPING AHEAD: The entire tutorial worked out great and the code in this repo is in
excellent condition and working order, a great starting point for a stack/app.

You could compare this with their own offical repo here:
https://github.com/testdrivenio/flask-on-docker

I hand coded everything here in my JimmyGizmo/gunipoc repo and nothing was cut
and paste from their tutorial or repo.

One of the best tutorials I have done and the end result is incredibly valuable
as a starting point for an excellent stack. I will be incorporating a lot of
great things from here into Nucleus. This turned out to be much more than just
switching from UWSGI to Gunicorn. I got a lot more out of it. I will even consider
purchasing courses from TestDriven.io. It was that good.





