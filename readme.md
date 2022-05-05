## Challenge Data Analytics - Python
_____________________________

#### Objetivo
Crear un proyecto que consuma datos desde
3 fuentes distintas para popular una base de datos SQL con información cultural
sobre bibliotecas, museos y salas de cines argentinos.

#### Ejecución del programa

##creacion de entorno virtual
Un entorno virtual permite separar las dependencias de un proyecto en particular de los paquetes instalados globalmente en una instalación de Python. Python incluye en su biblioteca estándar una utilidad para ello llamada venv. Para crear un nuevo entorno virtual se debe ejecutar el siguiente comando en la terminal:

python -m venv env


Esto creará un nuevo entorno virtual en la carpeta env. El comando típicamente se ejecuta desde la ruta en la cual se encuentran los archivos del proyecto para el cual se quiere crear el entorno. Por ejemplo:

mkdir nuevo_proyecto
cd nuevo_proyecto
python -m venv env


Una vez creado, el entorno virtual debe activarse vía alguno de los siguientes comandos.

En Windows:

env\Scripts\activate


En Linux y Mac OS:

source env/bin/activate


Activado el entorno virtual, utilizar normalmente los comandos python y pip para ejecutar la aplicación o instalar nuevos paquetes en el entorno.

**1) Clon del repositorio**

Clonar el proyecto
```cmd
git clone

```

**2) Configuración**

Copiar y renombrar el archivo `settings.template.ini` a `settings.ini`.
Completar las variables de configuración para establecer conexión a la base de datos.

**3) Instalación de dependencias**

```cmd
pip install -r requirements.txt
```

**4) Ejecución challenge**
```cmd
python src/main.py
```

#### Descripción de los archivos
- **src:** 
  - *datos.py*: proceso de adquisición de los datos desde la fuente, normalización de los mismos y creación de tablas con la información solicitada.
  - *main.py*: ejecuta programa completo, conexión a base de datos, creación de tablas en postgress desde archivo .sql y carga de datos creados por archivo datos.py.
  - *script*: contiene archivo .sql con scripts para la creación de tablas.
  - *data*: carpeta que va a almacenar las tablas descargadas desde la fuente original.
- **requirement.txt**: muestra las librerias y versiones utilizados para el desarrollo del programa.
- **settings.template.ini**: plantilla para configurar datos de conexión a base de datos.