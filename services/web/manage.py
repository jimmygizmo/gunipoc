from flask.cli import FlaskGroup

#### DEBUG 2
# Adding the following to try to inspect the DB/tables from here
from sqlalchemy import create_engine
engine = create_engine("postgresql://hello_flask:hello_flask@db:5432/hello_flask_prod")
from sqlalchemy import inspect
inspector = inspect(engine)
####

from project import app, db, User


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

