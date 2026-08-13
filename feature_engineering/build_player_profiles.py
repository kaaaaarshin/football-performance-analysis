import pandas as pd

df = pd.read_csv(
    "data/processed/player_match_dataset.csv"
)

player_profiles = (
    df.groupby("player")
    .agg({
        "passes": "mean",
        "successful_passes": "mean",
        "pass_accuracy": "mean",
        "shots": "mean",
        "goals": "mean",
        "dribbles": "mean",
        "pressures": "mean",
        "interceptions": "mean",
        "ball_recoveries": "mean",
        "duels": "mean",
        "blocks": "mean",
        "fouls_won": "mean",
        "fouls_committed": "mean"
    })
    .reset_index()
)

player_profiles.to_csv(
    "data/processed/player_profiles.csv",
    index=False
)

print(player_profiles.columns.tolist())