from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import CSRFProtect
# from flask_migrate import Migrate


# csrf = CSRFProtect()
from web import app

db = SQLAlchemy()
login_manager = LoginManager()


# migrate = Migrate()

def save_to_db(self):
    db.session.add(self)
    db.session.commit()


def delete(self):
    """
           Delete a model instance.
           :return: db.session.commit()'s result
           """
    db.session.delete(self)
    return db.session.commit()
