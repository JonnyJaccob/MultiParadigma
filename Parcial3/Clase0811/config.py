class BaseConf:
    USER_DB = 'postgres'
    PASS_DB = 'contra'
    URL_DB='localhost'
    PORT_DB = '5433' 
    NAME_DB = 'parcial3'
    FULL_URL_DB = f"postgresql://{USER_DB}:{PASS_DB}@{URL_DB}:{PORT_DB}/{NAME_DB}"

    SQLALCHEMY_DATABASE_URI = FULL_URL_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "llave_secreta"
    DEBUG = False 
    BCRYPT_LOG_ROUNDS = 13