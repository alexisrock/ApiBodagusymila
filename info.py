from fastapi import HTTPException
from database import get_connection

def get_user_info(pk_id_invitado: int):
    conn = get_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="No se pudo conectar a la base de datos.")
    
    cursor = conn.cursor()
    try:
        cursor.execute("EXEC get_user_info @pk_id_invitado = ?", pk_id_invitado)
        result = cursor.fetchall()
        
        # Convertir los resultados a JSON
        invitados = []
        for row in result:
            invitados.append({
                "id": row.pk_id_invitado,
                "nombre": row.nombre.strip(),
                "confirmado": row.confirmado,
                "asistencia": row.asistencia
            })

        return {
            "invitados": invitados
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error ejecutando el procedimiento almacenado: {str(e)}")
    finally:
        cursor.close()
        conn.close()
