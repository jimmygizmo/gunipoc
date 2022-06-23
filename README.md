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
did cause us to HAVE to upgrade flask, so sometimes there are issues from
going for the latest versions, but it is still the best strategy.

------------------------------------

I added this step to the Dockerfile, since if they are upgrading pip, well
I usually do both pip and setuptools.

RUN pip install --upgrade setuptools

--------------------------


