
<br>

<img align="left" width="250" height="90" src="https://raw.githubusercontent.com/marinsmh/senniors_challenge/main/imgs/senniors_icon.png">
<p vertical-align="middle"><h1>Senniors Python Challenge - June 2022</h1></p>

<br>

- [Objetivo](#objetivo)

## Objetivo

El objetivo de esta prueba es crear una API con dos endpoints para gestionar la suscripción a la newsletter de la empresa. 
Uno para imprimir aquellos usuarios que ya están en la BD y otro para añadir nuevos. 

Endpoint GET:

> Entrada: Ninguna
> 
> Salida:  Lista de usuarios suscritos

Endpoint POST:

> Entrada: Usuario de tipo NewUser con las propiedades propuestas en la definición de la prueba.
> 
> Salida:  Si ha ido bien devuelve ese mismo usuario añadido. En caso de fallo saldrá un mensaje de error.
	
## Setup ##

Este repositorio depende de:

*   sqlite3 como gestor de base de datos
    
		pip install sqlite3
        
* fastapi para las operaciones API/REST y Uvicorn para arrancar el servidor.
    
		pip install fastapi
        
		pip install uvicorn[standard]
        
* pydantic para el modelo de datos.
    
		pip install pydantic
		
Para arrancar el servidor utilizaremos el comando:

	python -m uvicorn main:app --reload
	
Donde main es el contenedor de los endpoints y app es el instance de la clase FastAPI.
	
## Formato del código ##

????

## Obtención de datos ##

??? Llamando a la url?

## Testing ##

	Creamos una prueba basada en test suit. 
