
<br>

<img align="left" width="250" height="90" src="https://raw.githubusercontent.com/marinsmh/senniors_challenge/main/imgs/senniors_icon.png"/>
<p vertical-align="middle"><h1>Senniors Python Challenge - June 2022</h1></p>

<br>

- [Descripción de la prueba](#descripción-de-la-prueba)
- [Requerimientos](#requerimientos)
- [Operaciones](#operaciones)
- [Setup](#setup)

## Descripción de la prueba

Senniors esta realmente comprometido con sus usuarios. En pro de ofrecerles buenas recomendaciones e información util, se ha creado el servicio SenniorsNews, una
newsletter semanal con noticias de interés sobre cuidados y salud. Varios usuarios se han apuntado ya, pero queremos crear una api que permita subscribirse a la newsletter sin necesidad de imputar los datos manualmente.

## Requerimientos 

**1. Crear una API con dos endpoints:**

	• POST /newsletter
	
		- Payload: la información de un nuevo usuario que se subscribe (name, email, birth_date, sennior_client)
		
		- Se debe almacenar en la base de datos
		
		- Se debe incluir la fecha de subscripción
		
		- Devuelve la información el usuario subscrito. Si ya existe devuelve un error con un mensaje acorde.
		 

	• GET /newsletter
	
		- Devuelve la lista de usuarios subscritos.

**2. Crear una DB para almacenar la información previa.**

**3. Insertar los usuarios ya subscritos en la DB con un script**

**4. Desplegar en AWS para poder acceder desde cualquier dispositivo.**

## Operaciones

Además he añadido una operación más con la que podemos borrar el contenido de la BD para limpiarla en caso de interesarnos.

| Resource | Method | Input | Output |
| :--- | :--- | :--- | :--- |
| /newsletter | GET | - | List usuarios suscritos |
| /newsletter | POST | newUser: {name, email, birth_date, sennior_client, suscription_date} | En caso de funcionar: el nuevo usuario suscrito. En caso de fallar: mensaje de error|
| /newsletter | DELETE | - | Mensaje OK en caso de haber eliminado todo corrctamente|

La estructura de Swagger UI:

## Setup

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

## Testing

Creamos una prueba basada en test suit. 

## AWS

El paquete aws intenta proporcionar soporte para el uso de Amazon Web Services como S3 (almacenamiento), SQS (colas) y otros a los programadores de Haskell. El objetivo final es dar soporte a todos los servicios web.
El concepto principal en aws es la Transacción, que corresponde a una única petición HTTP a los Servicios Web de Amazon. Una transacción consiste en una solicitud y una respuesta, que se asocian a través de la clase de tipo Transaction.


