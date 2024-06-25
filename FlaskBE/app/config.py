# config.py : Flask 애플리케이션 설정
import os


# application의 기본 디렉토리 경로 설정
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # 비밀키 : application 보안 관련 작업에 사용
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'dont-guess'

    # SQLAlchemy db URI 설정, SQLite,mysql 사용
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'myflaskapp.db')
    user = 'DE30_4nd_3'
    password = '7276'
    host = '192.168.0.80'
    port = '3306'
    database = 'de30_4nd_3'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + user + ':' + password + '@' + host + ':' + port + '/' + database

    '''
    # 여러개의 db를 사용하는 경우 
    SQLALCHEMY_BINDS = {
        'example2_db': 'sqlite:///' + os.path.join(basedir,'Phase1.db'),
        'example3_db': 'sqlite:///' + os.path.join(basedir,'example3.db'),
    }
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
