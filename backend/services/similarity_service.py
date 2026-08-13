import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv(
    "data/processed/player_profiles_clustered.csv"
)

features = [
    "passes",
    "successful_passes",
    "pass_accuracy",
    "shots",
    "goals",
    "dribbles",
    "pressures",
    "interceptions",
    "ball_recoveries",
    "duels",
    "blocks",
    "fouls_won",
    "fouls_committed"
]

scaler = MinMaxScaler()

X = scaler.fit_transform(df[features])

sim_matrix = cosine_similarity(X)


def get_similar_players(player_name, top_n=10):

    player_row = df[df["player"] == player_name]

    if player_row.empty:
         return {
            "error": f"Player '{player_name}' not found"
        }

    idx = player_row.index[0]

    scores = list(
        enumerate(sim_matrix[idx])
    )

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )[1:]

    results = []

    for i, score in scores[:top_n]:

        results.append({
            "player": df.iloc[i]["player"],
            "role": df.iloc[i]["role"],
            "similarity": round(score * 100, 2)
        })

    return results

def search_players(query):

    query = query.lower()

    matches = df[
        df["player"]
        .str.lower()
        .str.contains(query, na=False)
    ]

    return matches["player"].tolist()