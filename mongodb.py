import traceback
import pymongo

# Intentar establecer la conexión
try:
    client = pymongo.MongoClient(
        "mongodb+srv://extasys777:extasys777@cluster0.0g5viu0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )
    # Verificar si la conexión es exitosa
    client.admin.command('ping')
    print("MONGODB CONECTADO EXITOSAMENTE ✅")
except pymongo.errors.ConnectionError as e:
    print(f"Fallo la conexión a MongoDB ❌: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

# Acceder a las bases de datos y colecciones
try:
    folder = client["MASTER_DATABASE"]
    usersdb = folder.USERSDB
    chats_auth = folder.CHATS_AUTH
    gcdb = folder.GCDB
    sksdb = client["SKS_DATABASE"].SKS
    confdb = client["SKS_DATABASE"].CONF_DATABASE

    # Verificar si las colecciones existen (opcional, pero útil para evitar errores)
    print("Acceso a las colecciones exitoso ✅")
except Exception as e:
    print(f"Error al acceder a las colecciones o bases de datos: {e}")
    traceback.print_exc()
