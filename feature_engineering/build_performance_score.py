import pandas as pd

df = pd.read_csv(
    "data/processed/player_match_dataset.csv"
)

print(df.shape)

df["performance_score"] = (
    0.02 * df["successful_passes"]
    + 5 * df["goals"]
    + 0.5 * df["shots"]
    + 0.3 * df["dribbles"]
    + 0.2 * df["pressures"]
    + 1.0 * df["interceptions"]
    + 0.8 * df["ball_recoveries"]
    + 0.5 * df["duels"]
    + 0.5 * df["blocks"]
    + 0.2 * df["fouls_won"]
    - 0.2 * df["fouls_committed"]
)
"""
print(
    df[
        [
            "player",
            "performance_score"
        ]
    ]
    .sort_values(
        "performance_score",
        ascending=False
    )
    .head(20)
)
"""

top = df.sort_values(
    "performance_score",
    ascending=False
).head(20)

print(
    top[
        [
            "player",
            "goals",
            "shots",
            "successful_passes",
            "dribbles",
            "pressures",
            "performance_score"
        ]
    ]
)