from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth import authenticate_user
from confirmation import confirm_assistance
from info import get_user_info
from advice import insert_advice
from observation import update_observation
from suggestedSong import insert_suggested_song
from models import LoginRequest, ConfirmationRequest, AdviceRequest, ObservationRequest, SuggestedSongRequest

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.post("/login/")
async def login(request: LoginRequest):
    return authenticate_user(request)

@app.post("/confirm-assistance/")
async def confirm_assistance_endpoint(request: ConfirmationRequest):
    return confirm_assistance(request)

@app.get("/user-info/{pk_id_invitado}")
async def user_info(pk_id_invitado: int):
    return get_user_info(pk_id_invitado)

@app.post("/insert-advice/")
async def insert_advice_endpoint(request: AdviceRequest):
    return insert_advice(request)

@app.post("/update-observation/")
async def update_observation_endpoint(request: ObservationRequest):
    return update_observation(request)

@app.post("/insert-suggested-song/")
async def insert_suggested_song_endpoint(request: SuggestedSongRequest):
    return insert_suggested_song(request)