from fastapi import HTTPException
from database import get_connection
from models import LoginRequest

def authenticate_user(request: LoginRequest):
    conn = get_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="No se pudo conectar a la base de datos.")
    
    cursor = conn.cursor()
    try:
        password = request.password  # Extraer el password del objeto request
        cursor.execute("EXEC authenticate_user @password = ?", password)  # Usar el valor extraído
        result = cursor.fetchall()
        
        # Convertir los resultados a JSON
        invitados = []
        for row in result:
            invitados.append({
                "id": row.pk_id_invitado,
                "nombre": row.nombre.strip(),
                "confirmado": row.confirmado,
                "asistencia": row.asistencia,
                "cabeza_familia": row.cabeza_familia
            })

        # Determinar el ID principal basado en la lógica de cabeza de familia
        if len(invitados) > 1:
            id_principal = next((inv["id"] for inv in invitados if inv["cabeza_familia"] == 1), None)
        else:
            id_principal = invitados[0]["id"]

        return {
            "id": id_principal,
            "invitados": invitados
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error ejecutando el procedimiento almacenado: {str(e)}")
    finally:
        cursor.close()
        conn.close()
