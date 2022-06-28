#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv

# Abrimos el archivo CSV
f = open('newsletter.csv','r') 

reader = csv.reader(f, delimiter=',')

# Crea la BD en la carpeta donde se encuentra el script
sql = sqlite3.connect('Senniors.db')
cur = sql.cursor()

# Creamos la tabla si no existe
cur.execute('''CREATE TABLE IF NOT EXISTS newsletter
            (name text, email text PRIMARY KEY, birth_date date, sennior_client boolean, subscripted_date date)''')

# Llenamos la BD con los datos del CSV (convertido anteriormente de xlsx a csv)
for row in reader:
    cur.execute("INSERT INTO newsletter VALUES (?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4]))

# Imprimimos el contenido para ver si todo lo anterior ha ido bien
for row in cur.execute('SELECT * FROM newsletter'):
    print(row)

#Cerramos el archivo y la conexion a la bd y después cerramos conexión
f.close()
sql.commit()
sql.close()