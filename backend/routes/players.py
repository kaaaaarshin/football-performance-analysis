from fastapi import APIRouter
import pandas as pd

router = APIRouter()

# ==========================
# LOAD DATA
# ==========================

df = pd.read_csv(
    "data/processed/player_profiles_clustered.csv"
)

# ==========================
# GET ALL PLAYERS
# ==========================

@router.get("/players")
def get_players():

    return df["player"].tolist()

# ==========================
# SEARCH PLAYERS
# ==========================

@router.get("/search/{query}")
def search_players(query: str):

    results = df[
        df["player"]
        .str.lower()
        .str.contains(
            query.lower(),
            na=False
        )
    ]

    return results["player"].tolist()

# ==========================
# PLAYER PROFILE
# ==========================

@router.get("/player/{player_name}")
def get_player(player_name: str):

    player = df[
        df["player"] == player_name
    ]

    if player.empty:

        return {
            "error": f"Player '{player_name}' not found"
        }

    result = player.iloc[0].to_dict()

    for key, value in result.items():

        if isinstance(value, float):

            result[key] = round(
                value,
                2
            )

    return result

# ==========================
# COMPARE PLAYERS
# ==========================

@router.get("/compare/{player1}/{player2}")
def compare_players(
    player1: str,
    player2: str
):

    p1 = df[
        df["player"] == player1
    ]

    p2 = df[
        df["player"] == player2
    ]

    if p1.empty:

        return {
            "error": f"Player '{player1}' not found"
        }

    if p2.empty:

        return {
            "error": f"Player '{player2}' not found"
        }

    p1_data = p1.iloc[0].to_dict()
    p2_data = p2.iloc[0].to_dict()

    for data in [p1_data, p2_data]:

        for key, value in data.items():

            if isinstance(value, float):

                data[key] = round(
                    value,
                    2
                )

    return {
        "player1": p1_data,
        "player2": p2_data
    }

# ==========================
# STATS
# ==========================

@router.get("/stats")
def get_stats():

    return {
        "total_players": len(df),
        "roles": df["role"].nunique(),
        "clusters": df["cluster"].nunique(),
        "dataset": "LaLiga 2015-16"
    }

# ==========================
# ROLE DISTRIBUTION
# ==========================

@router.get("/role-distribution")
def role_distribution():

    counts = (
        df["role"]
        .value_counts()
        .to_dict()
    )

    return counts