import pymysql


class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Agus4551850.'
    MYSQL_DB = 'proyectofullstack'


config = {
    'development': DevelopmentConfig
}




def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='Agus4551850.',
                                db='proyectofullstack')
