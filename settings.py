# -*- coding: utf-8 -*-

# FLASK_ENV = 'development' #development
DEBUG = True
DEBUG_HOST = '0.0.0.0'
DEBUG_PORT = 1238

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4'.format(
        user='cms',
        password='cms',
        host='192.168.1.105',
        port=3306,
        database='surl')
)

INIT_FIRST_SEQ = 1000000
# pip freeze > requirement.txt
