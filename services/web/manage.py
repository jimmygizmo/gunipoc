from flask.cli import FlaskGroup

from project import app, db


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
@cli.command("db_debug")
def db_session_debug():
    print()
    print()
    print(help(db.session))
    print()
    print()
    print()
    print()
    dir(db.session)
    print()
    print()
    print()
    print()
    print(db.session)
    print()
    print()


if __name__ == "__main__":
    cli()

