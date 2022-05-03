#Obtener los 3 archivos de fuente utilizando la librería requests y

import requests 
import pandas as pd
import io
import os
from datetime import date
from datetime import datetime
import logging

logging.basicConfig( level=logging.DEBUG, filename='loggin.log')

logger = logging.getLogger('loggin')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
# logger.debug('mensaje debug')
# logger.info('mensaje info')
# logger.warning('mensaje warning')
# logger.error('mensaje error')
# logger.critical('mensaje critical')

#obtener archivos

urlMuseos= 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'
urlCines= 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
urlBibliotecas = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'

rMuseos = requests.get(urlMuseos) 
rCines = requests.get(urlCines) 
rBibliotecas = requests.get(urlBibliotecas)
logger.info('mensaje info')
#Organizar los archivos
museosCSV=pd.read_csv(io.StringIO(rMuseos.content.decode('utf-8')))
museos=pd.DataFrame(museosCSV)

cinesCSV=pd.read_csv(io.StringIO(rCines.content.decode('utf-8')))
cines=pd.DataFrame(cinesCSV)

bibliotecasCSV=pd.read_csv(io.StringIO(rBibliotecas.content.decode('utf-8')))
bibliotecas=pd.DataFrame(bibliotecasCSV)




#Crear directorio de destino si no existe
ROOT_DATA_PATH = './data'

anio = date.today().year
mes = datetime.now().strftime("%B")
dia = datetime.now().strftime("%d")


dirNameMuseos = ( ROOT_DATA_PATH + '/museos/'+str(anio)+'-'+str(mes)+'/')
dirNameCines = (ROOT_DATA_PATH + '/cines/'+str(anio)+'-'+str(mes)+'/')
dirNameBibliotecas = (ROOT_DATA_PATH + '/bibliotecas/'+str(anio)+'-'+str(mes)+'/')

print(dirNameBibliotecas)
print(dirNameCines)
print(dirNameMuseos)

#guardarlos en la carpeta fuentes



if not os.path.exists(dirNameMuseos):
    os.makedirs(dirNameMuseos)
    print("Directory " , dirNameMuseos ,  " Created ")
else:
    print("Directory " , dirNameMuseos ,  " already exists")

if not os.path.exists(dirNameCines):
    os.makedirs(dirNameCines)
    print("Directory " , dirNameCines ,  " Created ")
else:
    print("Directory " , dirNameCines ,  " already exists")

if not os.path.exists(dirNameBibliotecas):
    os.makedirs(dirNameBibliotecas)
    print("Directory " , dirNameBibliotecas ,  " Created ")
else:
    print("Directory " , dirNameBibliotecas ,  " already exists")
logger.info('mensaje info: se crean los directorios de destino')

#guardar los archivos en la carpeta fuentes

nMuseos= dirNameMuseos+'museos'+ '-'+str(dia)+ '-'+str(mes)+'-'+str(anio)+ '.csv'
nSalasCine = dirNameCines+'cines'+ '-'+str(dia)+ '-'+str(mes)+'-'+str(anio)+ '.csv'
nBibliotecas = dirNameBibliotecas+'bibliotecas'+ '-'+str(dia)+ '-'+str(mes)+'-'+str(anio)+ '.csv'


museos.to_csv(nMuseos, index=False)
cines.to_csv(nSalasCine, index=False)
bibliotecas.to_csv(nBibliotecas, index=False)
logger.info('mensaje info: se guardan los archivos en la carpeta fuentes')




