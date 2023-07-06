import csv
import json
import couchdb

# Conexión al servidor CouchDB
couch = couchdb.Server('http://admin:admin@localhost:5984') 

# Seleccionar o crear una base de datos existente
nombre_base_datos = 'corecion'  # Reemplaza con el nombre deseado para tu base de datos
db = couch[nombre_base_datos]

def csv_a_json(archivo_csv):
    # Abrir el archivo CSV
    with open(ruta_archivo_csv, 'r', encoding='utf-8') as archivo_csv:
        # Leer el contenido del archivo CSV
        contenido_csv = csv.DictReader(archivo_csv)

        
        contenido_json = [fila for fila in contenido_csv]

    return contenido_json

# Especificar la ruta del archivo CSV
ruta_archivo_csv = 'C:\\Users\\TU PUNTO NET\\imdb_movies.csv'

# Convertir CSV a JSON
contenido_json = csv_a_json(ruta_archivo_csv)

# Subir el JSON a la base de datos
for documento in contenido_json:
    db.save(documento)

print("El archivo CSV se ha subido correctamente a CouchDB.")