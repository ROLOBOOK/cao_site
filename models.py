from app import db
from flask_security import UserMixin, RoleMixin



### таблица для отношения многие ко многим
roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)


class Role(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __init__(self,*args, **kwargs):
        super(Role,self).__init__(*args,**kwargs)

    def __repr__(self):
        return f'Role {self.name}'


class User(db.Model,RoleMixin):
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    active = db.Column(db.Boolean())
    email = db.Column(db.String(100), unique=True)
    roles = db.relationship('Role', secondary=roles_users, backref='users')

    def __init__(self,*args,**kwargs):
        super(User, self).__init__(*args,**kwargs)

    def __repr__(self):
        return f'User {self.name}'


