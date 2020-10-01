# SIMPLEQL CLI - MANUAL DE USUARIO

SimpleQL es un lenguaje de consultas que funciona únicamente a nivel de consola, su
propósito es facilitar al usuario la búsqueda de registros completos en archivos AON, en los
que buscar registro por registro podría ser muy tedioso y cansado

### ARCHIVOS DEL PROYECTO

- `README.md` con manual de usuario, instrucciones de instalación, uso y
  documentación del API.
- `aon.py`: script que lee el archivo aon y los guarda en memoria
- `automatas.py`: Contiene los AFD que analiza los comandos ingresados 
- `comandos.py`, Realiza las acciones para cada comando ingresado
- `comandos.siql` SIQL de prueba que contiene comandos 
- `createSet.py`: Objeto set donde están guardado el nombre y los registros ingresados de cada set
- `header.txt`: Texto que contiene el header de la plantilla de HTML 
- `main.py`, Script principal que comieza el programa
- `prueba.aon`: Archivo AON para hacer pruebas de carga 
- `regex.py`, script que hace comaparaciones de texto con expresioes regulares
- `seleccionar.py` Se ejecutan todos los SELECT
- `siql.py`: Enaliza los SCRIPT SIQL y los ejecuta
- `.gitignore` para ignorar `node_modules` u otras carpetas que no deban
  incluirse en control de versiones (`git`).

## COMANDOS

### 1. CREATE SET < ID >
Tiene la función de crear sets de memoria donde se alojarán ciertos conjuntos de
datos cargados por el usuario. La aplicación tiene la capacidad de poseer activos N
conjuntos de datos.
* Se ejecuta escribiendo:
```
CREATE SET carros
CREATE SET elementos
```
*  Al ejecutar este comando se creara un set en memoria con el nombre ingresado y se devolverá un mensaje de éxito.

### 2. LOAD INTO < set_id > FILES < id > [ , <id> ] +
Este comando carga al conjunto especificado por set_id la información contenida en
la los archivos de la lista de archivos definida después de la keyword FILES.
* Se ejecuta escribiendo:
```
LOAD INTO elementos FILES periodica.aon, periodica2.aon
LOAD INTO carros FILES carros.aon
``` 

### 3. USE SET < set_id >
Este comando define el set de datos a utilizar para las siguientes operaciones.
* Se ejecuta con:
```
USE SET carros
USE SET elementos
```
* Si se ejecutan los comandos siquientes sin haber definido el set a usar mostrará un mensaje de error.

### 4. SELECT < atributo > [ , <atributo>] + [ WHERE < condiciones > ]
Permite seleccionar uno o más registros o atributos de los mismos con base en
condiciones simples que pueden aplicarse a los atributos de los mismos.
* Se ejecuta con:
```
SELECT modelo, tipo, marca, año WHERE color = “rojo”
SELECT *
SELECT * WHERE marca = “Mazda” AND año < 1996
```
* Con asterisco `SELECT *` nos muestra todos los registros cargados.
* Se podrá utilizar los operadores `<` (menor que), `>` (mayor que), `<=` (menor igual), `>=` (mayor igual), `=` (igual) y `!=` (no igual).
* También podran combinarse condiciones con `OR`, `AND` y `XOR`.
```
SELECT nombre, padre, siglas WHERE tipo = “metal” OR tipo = “carbono”
SELECCIONAR * WHERE siglas = “HG”
```
* Y se podrán hacer comparaciones con expresiones regulares con `REGEX`
```
SELECT * WHERE nombre REGEX [^a|^b|^O|ab.+]
```
### 5. LIST ATTRIBUTES
Este comando permite listar los atributos que componen a cada registro del set.
* Estructura:
```
LIST ATTRIBUTES
```
 
### 6. PRINT IN <color>

Este comando permite al usuario elegir el color en el que serán presentados los
resultados en la línea de comandos. Los valores a elegir serán `BLUE`, `RED`, `GREEN`,
`YELLOW`, `ORANGE` y `PINK`.
* Estructura:

```
PRINT IN BLUE
```
### 7. MAX < atributo > | MIN < atributo >
Permiten encontrar el valor máximo o el valor mínimo que se encuentre en el
atributo de uno de los registros del conjunto en memoria.

* Estructura:
```
MAX año
MIN modelo 
```
### 8. SUM < atributo > [, <atributo> ] +
Permite obtener la suma de todos los valores de un atributo especificado en el
comando.

* Se utiliza escribiendo 
```
SUM edad, promedio, faltas
SUM asistencias
SUM *
```
* El comando `SUM` acepta el uso del operador `*`.

### 9. COUNT < atributo > [, < atributo > ] +
Permite contar el número de registros que se han cargado a memoria. En caso de
que alguno de los atributos tenga valor null se ignorará. El comando `COUNT`
permite el uso del operador `*`.

* Se utiliza escribiendo:
```
COUNT *
COUNT edad, promedio, faltas
```
### 10.REPORT TO < id > < comando >
Este comando permite crear un reporte en html a partir de cualquier otro comando
de análisis o selección.
* Se utiliza escribiendo:
```
REPORT TO reporte1 COUNT *
REPORT TO reporte2 SUM *
REPORT TO reporte3 SELECT * WHERE edad != 44
```
* El `id` define el nombre del archivo sobre el que se crea el reporte.

### 11.SCRIPT < direccion > [, < direccion > ]
Este comando permite cargar scripts con extensión .siql que contienen series de
instrucciones y comandos SimpleQL.
* Se utiliza escribiendo:
```
SCRIPT comandos.siql
```
### 12. REPORT TOKENS
Este comando crea un reporte en html que muestra una lista de todos los
lexemas encontrados por el AFD

## CLONAR
Para poder ejecutar el programa se tiene que clonar o simplemente descargar los archivos.

* Para clonar, rimero se ejecuta el git bash en la carpeta donde se desea descargar el proyecto
![](includes/preview/1.png)

* Luego escribies el comando 
```
git clone https://github.com/201700900/-Proyecto1-LFP.git
```
![](includes/preview/5.png)
* Y eso es todo, ya puedes probar el programa ejecutandolo o ver los scripts.



## Librerias requeridas

* [tabulate](https://pypi.org/project/tabulate/) 
* [pandas](https://pandas.pydata.org/docs/index.html)
* [webbrowser](https://rometools.github.io/rome/)


## CÓMO USAR
El programa consta de 12 comandos muy faciles de usar.
  Pero antes de se debe ejecutar el el programa deberá clonar o descargar los archivos del proyecto.
*  Para clonar primero se abre el Simbolo del Sistema, CMD.
* Se va a la carpeta del programa `201700900_Proyecto1_LFPA`
  cambiando de directorio 
  con el comando `cd <path>201700900_Proyecto1_LFPA`
   ![](includes/preview/2.png)
  
* Ya en la carpeta del programa se escribe `python main.py`
    ![](includes/preview/3.png)
  
* Y ya se está listo para ingresar un comando
  ![](includes/preview/4.png)
