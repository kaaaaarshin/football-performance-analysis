from fastapi import APIRouter

from backend.services.similarity_service import (
    get_similar_players
)

router = APIRouter()

@router.get("/similar/{player_name}")
def similar_players(player_name: str):

    return get_similar_players(
        player_name
    )