from pymongo import MongoClient
from pymongo.server_api import ServerApi

MONGODB_URL = "mongodb+srv://slopeztr:<password>@clustertest.thk7dlx.mongodb.net/?retryWrites=true&w=majority&appName=ClusterTest"


def connect() :
    client = MongoClient(MONGODB_URL, server_api=ServerApi('1'))
    
    try:
        client.admin.command('ping')
        print("Su conexión fue satisfactoria a MongoDB!")
    except Exception as e:
        print(e)
    
    return client

# Crear la conexión a la base de datos
conn = connect()

# Referencias a la db 
db = conn.torneos

# Referencias a la colección
equipos_collection = db.equipos


new_equipo = { 
    "nombre": "Equipo F", 
    "ciudad": "Ciudad F", 
    "jugadores": ["Jugador 1", "Jugador 6", "Jugador 7", "Jugador 8", "Jugador 9"] 
}

# Insertar nuevo equipo en la colección
result = equipos_collection.insert_one(new_equipo)

# Consultar la colección
equipos = equipos_collection.find()

# Itera sobre los documentos y haz algo con ellos
for equipo in equipos:
    print(equipo)

conn.close()