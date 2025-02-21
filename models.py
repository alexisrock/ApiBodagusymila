from pydantic import BaseModel
from typing import List, Optional

class LoginRequest(BaseModel):
    password: str

class Invitado(BaseModel):
    id: int
    confirmado: int
    asistencia: Optional[int]

class ConfirmationRequest(BaseModel):
    invitados: List[Invitado]

class AdviceRequest(BaseModel):
    pk_id_invitado: int
    consejo: str

class ObservationRequest(BaseModel):
    pk_id_invitado: int
    observacion: str

class SuggestedSongRequest(BaseModel):
    pk_id_invitado: int
    url_cancion: str
    momento_cancion: str