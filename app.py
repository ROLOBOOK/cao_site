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
from flask_security import current_user

from flask_admin import AdminIndexView
from flask  import redirect, url_for, request


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


class AdminMixin:
    def is_accessible(self): #- проверяет доступность вьюхи пользователю
        return current_user.has_role('admin')


    def inaccessible_callback(self,name, **kwargs): #-если пользователю не доступна вбюхе
        return redirect(url_for('security.login', next=request.url )) #переводим на страницу авторизации


class AdminView(AdminMixin,ModelView):
    pass

class HomeAdmin(AdminMixin,AdminIndexView):
    pass

admin = Admin(app, 'CAO_admin', url='/', index_view=HomeAdmin(name='Home'))

admin.add_view(AdminView(User, db.session)) #  связываем таблица с админкой. вытаскивает из базы и показывает в иеб интерфейсе
admin.add_view(AdminView(Role, db.session))
admin.add_view(AdminView(Count_defect_zondes, db.session))





user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


