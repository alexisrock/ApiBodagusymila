from fastapi import HTTPException
from database import get_connection
from models import ConfirmationRequest, Invitado

def confirm_assistance(request: ConfirmationRequest):
    conn = get_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="No se pudo conectar a la base de datos.")
    
    cursor = conn.cursor()
    try:
        for invitado in request.invitados:
            cursor.execute("EXEC confirm_assistance @pk_id_invitado = ?, @assistance = ?", invitado.id, invitado.asistencia)
        
        # Confirmar la transacción si todo fue exitoso
        conn.commit()
        return {"message": "Confirmación de asistencia realizada correctamente"}
    
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error al confirmar asistencia: {str(e)}")
    
    finally:
        cursor.close()
        conn.close()
