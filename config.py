import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))

    ENV = str(os.environ.get("ENV"))
    if ENV == "PROD":
        CONNECTION_STRING = str(os.environ.get("CONNECTION_STRING"))

        '''
        use this URI for migrating at CLOUD SQL
        '''
        SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://root:{PASSWORD}@{HOST}/{DATABASE}?unix_socket=/cloudsql/{CONNECTION_STRING}"

        # SQLALCHEMY_DATABASE_URI= f"mysql+mysqldb://root:{PASSWORD}@/{DATABASE}?unix_socket=/cloudsql/{PROJECT_ID}:us-central1:{INSTANCE_NAME}"

    else:
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + \
            ':' + PASSWORD + '@' + HOST + '/' + DATABASE

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True
