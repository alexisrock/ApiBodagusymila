from fastapi import HTTPException
from database import get_connection
from models import ObservationRequest

def update_observation(request: ObservationRequest):
    conn = get_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="No se pudo conectar a la base de datos.")
    
    cursor = conn.cursor()
    try:
        pk_id_invitado = request.pk_id_invitado
        observation = request.observacion
        cursor.execute("EXEC update_tip_nota_observacion @pk_id_invitado = ?, @observacion = ?", (pk_id_invitado, observation))
        
        #result = cursor.fetchone()
        return {"message": "Observacion registrada con exito"}
        conn.commit()
    
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error al registrar observacion: {str(e)}")
    
    finally:
        cursor.close()
        conn.close()
