import pandas as pd
import logging 
import numpy as np
from datetime import datetime
from datetime import date



logging.basicConfig(level=logging.DEBUG, filename='debug.log')
logger = logging.getLogger('loggin')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


dataBibliotecas = pd.read_csv('data/bibliotecas/2022-May/bibliotecas-02-May-2022.csv', delimiter=',')
dataBibliotecas.shape
dataCines = pd.read_csv('data/cines/2022-May/cines-02-May-2022.csv', delimiter=',')
dataCines.shape
dataMuseos = pd.read_csv('data/museos/2022-May/museos-02-May-2022.csv', delimiter=',')
dataMuseos.shape

nombre_columnas={'Cod_Loc':'Cod_localidad',
                'IdProvincia':'Id_provincia',
                'IdDepartamento':'Id_departamento',
                'Observacion':'Observaciones',
                'categoria':'Categoría',
                'subcategoria':'Subcategoria',
                'provincia':'Provincia',
                'Provincia':'Provincia',
                'departamento':'Departamento',
                'localidad':'Localidad',
                'nombre':'Nombre',
                'direccion':'Domicilio',
                'Dirección':'Domicilio',
                'piso':'Piso',
                'CP':'Código_Postal',
                'cod_area':'Cod_tel',
                'telefono':'Teléfono',
                'mail':'Mail',
                'web':'Web'
                                
                   
                }
bibliotecas = dataBibliotecas.rename(columns=nombre_columnas)
cines = dataCines.rename(columns=nombre_columnas)
museos = dataMuseos.rename(columns=nombre_columnas)

logger.info('mensaje info: se han renombrado las columnas')

#crear una unica tabla
culturaMain = pd.concat([museos,cines,bibliotecas])
logger.info('mensaje info: se ha unificado las tablas')
culturaMain.shape

cultura= culturaMain.loc[:,['Cod_localidad','Id_provincia', 'Id_departamento','Categoría','Provincia', 'Localidad', 'Nombre',
       'Domicilio','Código_Postal','Teléfono', 'Mail', 'Web']]

cultura=cultura.replace('s/d',np.nan)
print(cultura.head())
logger.info('mensaje info: se han creado las tablas')



# Agregamos columna de fecha de carga
culturaMain['Fecha carga']= datetime.today().strftime('%d-%m-%Y')


# Tabla registros
tabla_registros=pd.DataFrame(culturaMain.groupby(['Categoría','Fuente','Provincia']).size(), columns=['Totales'])
tabla_registros.drop(['Totales'], axis=1, inplace=True)

#Creamos tablas intermedias con la información solicitada
categoria= pd.DataFrame(culturaMain.groupby(['Categoría']).size(),columns=['Total por categoría'])  #Cantidad de registros totales por categoría
fuente=pd.DataFrame(culturaMain.groupby(['Fuente']).size(),columns=['Total por fuente'])    #Cantidad de registros totales por fuente
categoria_provincia= pd.DataFrame(culturaMain.groupby(['Categoría','Provincia']).size(),columns=['Total categoría por provincia'])   #Cantidad de registros por provincia y categoría

#Juntar información para formación de tabla
reg_cat= tabla_registros.merge(categoria, how='inner', left_index=True, right_index=True)
reg_cat_fue=reg_cat.merge(fuente, how='inner', left_index=True, right_index=True)
tabla_registros_merge=reg_cat_fue.merge(categoria_provincia, how='inner', left_index=True, right_index=True)
registros= tabla_registros_merge.reset_index()  # Resetear index
registros['Fecha carga']= datetime.today().strftime('%d-%m-%Y') # Agregar columna de fecha de carga
print(registros.head())







#Procesar la información de cines para poder crear una tabla que contenga Provicia, cantidad de pantallas, cantidad de butacas, cantidad de espacios INCAA

cines['Categoría'] = 'Cines'
cines['Subcategoria'] = 'Pantallas'
cines['INCAA'] = 1



cines_filtrados = cines.loc[:,['Provincia','Pantallas','Butacas', 'INCAA']]

cines_filtrados = cines_filtrados.groupby('Provincia').sum()

print(cines_filtrados)
logger.info('mensaje info: se han calculado los registros por provincia y categoría')







