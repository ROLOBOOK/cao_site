from app import db
from flask_security import UserMixin, RoleMixin



### таблица для отношения многие ко многим
roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __init__(self,*args, **kwargs):
        super(Role,self).__init__(*args,**kwargs)

    def __repr__(self):
        return f'Role {self.name}'


class User(db.Model,UserMixin):
    id =  db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))
    active = db.Column(db.Boolean())
    email = db.Column(db.String(100), unique=True)
    roles = db.relationship('Role', secondary=roles_users, backref='users')

    def __init__(self,*args,**kwargs):
        super(User, self).__init__(*args,**kwargs)

    def __repr__(self):
        return f'User {self.email}'



class Count_defect_zondes(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    s_n = db.Column(db.String(100), unique=True,nullable=False)
    type_zondes = db.Column(db.String(100), nullable=False)
    svch_5 = db.Column(db.String(1))
    chastota_6 = db.Column(db.String(1))
    chastota_7 = db.Column(db.String(1))
    pause_8 = db.Column(db.String(1))
    impuls_9 = db.Column(db.String(1))
    komutaciy_10 = db.Column(db.String(1))
    telemetriy_11 = db.Column(db.String(1))
    other_12 = db.Column(db.String(1))
    temper_13 = db.Column(db.String(1))
    vlaga_14 = db.Column(db.String(1))
    primechanie_15 = db.Column(db.String(100))
    date = db.Column(db.DateTime)


class Total_number_zondes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    type_zondes = db.Column(db.String(100), nullable=False)
    total_chek_zondes = db.Column(db.Integer)
