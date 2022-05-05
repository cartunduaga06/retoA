import logging
from sqlalchemy import create_engine
import psycopg2
from procesamientoDatos import culturaMain, registros, cines_filtrados
from datetime import datetime
from datetime import date


logging.basicConfig( level=logging.DEBUG, filename='loggin.log')

logger = logging.getLogger('loggin')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

logger.info('mensaje info: se ha iniciado creacion de sql')

DATABASE_NAME = 'cultura'
DATABASE_USERNAME = 'postgres' 
DATABASE_PASSWORD = 'postgres'

db_name = DATABASE_NAME if DATABASE_NAME else input('Database: ')
user = DATABASE_USERNAME if DATABASE_USERNAME else input('Username: ')
password = DATABASE_PASSWORD if DATABASE_PASSWORD else input('Password: ')

engine=create_engine('postgresql+psycopg2://'+user+':'+password+'@localhost:5432/'+db_name)
conn= engine.connect()

logging.info('Creando tablas en base de datos')
with open('/schemas.sql', 'r') as myfile:
    data = myfile.read()
conn.execute(data)

logger.info('subiendo información a la base de datos')

#Cargar datos a las tablas creadas en postgres
cines_filtrados.to_sql('salas_de_cine', con=engine, if_exists='replace')
registros.to_sql('registros', con=engine, if_exists='replace')
culturaMain.to_sql('cultura', con=engine, if_exists='replace')

conn.close()

logging.info('Fin de proceso')