from fastapi import HTTPException
from database import get_connection
from models import SuggestedSongRequest

def insert_suggested_song(request: SuggestedSongRequest):
    conn = get_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="No se pudo conectar a la base de datos.")
    
    cursor = conn.cursor()
    try:
        pk_id_invitado = request.pk_id_invitado
        url_song = request.url_cancion
        moment_song = request.momento_cancion
        cursor.execute("EXEC insert_sugerir_cancion @pk_id_invitado = ?, @url_cancion = ?, @momento_cancion = ?", (pk_id_invitado, url_song, moment_song))
        conn.commit()
        return {"message": "Cancion registrada correctamente"}
    
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error al registrar la cancion: {str(e)}")
    
    finally:
        cursor.close()
        conn.close()
