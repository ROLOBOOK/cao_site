from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import UserMixin, RoleMixin
from flask_security import SQLAlchemyUserDatastore
from flask_security import Security


#создаем приложение
app = Flask(__name__)

#откуда брать конфиг для приложения
app.config.from_object(Config)

# регистрируем базу
db = SQLAlchemy(app)


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand) # создаем команду для миграциaи

from models import *


admin = Admin(app)
admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(Role,db.session))



user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
