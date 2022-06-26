# Importa el módulo sqlite3
import sqlite3 
from fastapi import FastAPI
from datetime import datetime
from models import NewUser

app = FastAPI()

# http://127.0.0.1:8000/newsletter/
@app.get("/newsletter/")
async def read_users():

    # Crea un objeto de conexión a la base de datos SQLite
    conexion = sqlite3.connect("Senniors.db")
    # Con la conexión, crea un objeto cursor
    cursor = conexion.cursor()

    users_list=[]

    # El resultado de "cursor.execute" puede ser iterado por fila
    for row in cursor.execute('SELECT * FROM newsletter;'):
        users_list.append(row)

    conexion.close()

    return users_list


@app.post("/newsletter/")
async def insert_new_users(new_User: NewUser):
    
    conexion = sqlite3.connect("Senniors.db")

    fechaActual = datetime.today().strftime('%d/%m/%Y')
    new_User.subscripted_date = fechaActual #datetime.strptime(fechaActual, '%d/%m/%Y')

    try:
        conexion.execute("insert into newsletter values (?,?,?,?,?)", (new_User.name, new_User.email, new_User.birth_date, new_User.sennior_client, new_User.subscripted_date))
        conexion.commit()
    except sqlite3.IntegrityError:
        print("ERROR: Ese usuario ya está suscrito")

    conexion.close()

    return new_User