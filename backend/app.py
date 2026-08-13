from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.players import router as player_router
from backend.routes.recommendations import router as recommendation_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(player_router)
app.include_router(recommendation_router)