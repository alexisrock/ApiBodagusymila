import pyodbc

DATABASE_CONFIG = {
    "driver": "{ODBC Driver 18 for SQL Server}",
    "server": "tcp:serverwedding.database.windows.net,1433",
    "database": "wedding",
    "username": "Administrador_weeding",
    "password": "QcGr80vdfJ",
    "encrypt": "yes",
    "trust_server_certificate": "yes",
    "timeout": "30"
}

def get_connection():
    try:
        connection = pyodbc.connect(
            f"DRIVER={DATABASE_CONFIG['driver']};"
            f"SERVER={DATABASE_CONFIG['server']};"
            f"DATABASE={DATABASE_CONFIG['database']};"
            f"UID={DATABASE_CONFIG['username']};"
            f"PWD={DATABASE_CONFIG['password']};"
            f"Encrypt={DATABASE_CONFIG['encrypt']};"
            f"TrustServerCertificate={DATABASE_CONFIG['trust_server_certificate']};"
            f"Connection Timeout={DATABASE_CONFIG['timeout']};"
        )
        print("Conexión a la base de datos exitosa.")
        return connection
    except pyodbc.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None
