from flask.cli import FlaskGroup
# from project import app, db, User, config  # Importing config here was experimental.
from project import app, db, User  # We can get config the Flask way through app.

# If we wanted shorter config naming:
# from project import config.Config as cfg  # This does not work. Bad syntax.
# Cannot say config.Config here. ANYHOW, Flask has it's own config method.
# Let's try what the app is already doing, although not in this file yet.
# (We remove the import of 'config' that did work for this :
# config.Config.SQLALCHEMY_DATABASE_URI but is not necessarily the way we want.)
# Flask way. Will try:
# app.config["SQLALCHEMY_DATABASE_URI"]


#### DEBUG 2
# Adding the following to try to inspect the DB/tables from here
from sqlalchemy import create_engine
#engine = create_engine("postgresql://hello_flask:hello_flask@db:5432/hello_flask_prod")

#engine = create_engine(config.Config.SQLALCHEMY_DATABASE_URI)
# Shorter variant using variant import above:
#engine = create_engine(cfg.SQLALCHEMY_DATABASE_URI)  # Did not work out at import.

# This works. TODO: Research pro/cons of doing config the Flask way like this.
# I have my own clean/lightweight strategy which may or may not be a good way as I
# am still assessing and refining it, but it involves using just the namespace and
# not even creating a class, but rather just a dictionary called settings in a
# global config namespace. There are many ways to do it. I will give the full Flask
# methodology a study and a fair go before choosing a method for the Python app code
# of Nucleus. If you App code would benefit from a non-Flask configuration strategy
# then don't be afraid to do it. Have good reasons though. But you are not required
# to use any feature of a library, but you are required to understand why or why not,
# at least if you want to be a good developer you need good justifications based
# on research, testing, experience and standards appreciation.
engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])  # The Flask config way.


from sqlalchemy import inspect
inspector = inspect(engine)
####



cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

# To use this command:
# docker-compose exec web python manage.py create_db


@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="user@example.com"))
    db.session.commit()

# To use this command:
# docker-compose exec web python manage.py seed_db


# This did not reveal any method in session which could list or show all objects. I am debugging based on User not
# seeming to be recognized as a 'name' in the session, like as if the class/table was never defined.
# TODO: Fixed issue. import User was missing. This debug code can be removed now.
@cli.command("db_debug")
def db_debug():

    print("\n\n")
    print(help(db.session))
    print("\n\n")
    print(db.session)
    print("\n\n")


# TODO: Fixed issue. import User was missing. This debug code can be removed now.
@cli.command("db_debug2")
def db_debug2():
    for table_name in inspector.get_table_names():
        print("Table: %s" % table_name)
        for column in inspector.get_columns(table_name):
            print("  Column: %s" % column['name'])
        print()


if __name__ == "__main__":
    print("The __main__ section in manage.py just executed. It's not important. I'm just telling you.")
    cli()

