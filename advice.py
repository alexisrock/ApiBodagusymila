from fastapi import HTTPException
from database import get_connection
from models import AdviceRequest

def insert_advice(request: AdviceRequest):
    conn = get_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="No se pudo conectar a la base de datos.")
    
    cursor = conn.cursor()
    try:
        pk_id_invitado = request.pk_id_invitado
        consejo = request.consejo
        cursor.execute("EXEC insert_consejo @pk_id_invitado = ?, @consejo = ?", (pk_id_invitado, consejo))
        conn.commit()
        return {"message": "Consejo insertado correctamente"}
    
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error al insertar consejo: {str(e)}")
    
    finally:
        cursor.close()
        conn.close()