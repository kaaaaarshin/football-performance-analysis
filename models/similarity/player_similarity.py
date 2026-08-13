import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv(
    "data/processed/player_roles.csv"
)

features = df.drop(
    columns=[
        "player",
        "cluster",
        "role"
    ]
)

scaler = StandardScaler()

X_scaled = scaler.fit_transform(
    features
)

similarity_matrix = cosine_similarity(
    X_scaled
)

def find_similar_players(
    player_name,
    top_n=10
):

    player_index = df[
        df["player"] == player_name
    ].index

    if len(player_index) == 0:

        print(
            f"{player_name} not found"
        )

        return

    player_index = player_index[0]

    similarity_scores = (
        similarity_matrix[player_index]
    )

    similar_indices = (
        similarity_scores
        .argsort()[::-1]
    )

    similar_indices = similar_indices[
        1:top_n+1
    ]

    results = df.iloc[
        similar_indices
    ][
        ["player", "role"]
    ]

    print(
        f"\nMost Similar To {player_name}\n"
    )

    print(results)

print(
    df[df["player"] == "Sergio Ramos García"]
)

print(
    df[df["player"] == "Aymeric Laporte"]
)

print(
    df[df["player"] == "Shkodran Mustafi"]
)