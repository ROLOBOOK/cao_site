class Config(object):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://fol:Qq123456@localhost/cao_site' # connect base, conector, name user pasword addres_base name databas
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'CSFR'
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH =  'des_crypt'
