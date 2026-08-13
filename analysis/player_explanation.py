import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv(
    "data/processed/player_profiles_clustered.csv"
)

player1 = "Sergio Ramos García"
player2 = "Aymeric Laporte"

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

# -----------------------------
# Extract players
# -----------------------------

p1 = df[df["player"] == player1].iloc[0]
p2 = df[df["player"] == player2].iloc[0]

# -----------------------------
# Standardize
# -----------------------------

scaler = StandardScaler()

scaled = scaler.fit_transform(
    df[features]
)

scaled_df = pd.DataFrame(
    scaled,
    columns=features
)

idx1 = df[df["player"] == player1].index[0]
idx2 = df[df["player"] == player2].index[0]

vec1 = scaled_df.iloc[idx1]
vec2 = scaled_df.iloc[idx2]

# -----------------------------
# Similarity
# -----------------------------

sim = cosine_similarity(
    [vec1],
    [vec2]
)[0][0]

print("\n" + "="*50)
print(f"{player1}")
print("vs")
print(f"{player2}")
print("="*50)

print(
    f"\nSimilarity Score: {sim*100:.2f}%"
)

print("\nFeature Differences:\n")

diffs = []

for feature in features:

    diff = abs(
        p1[feature] - p2[feature]
    )

    diffs.append(
        (feature, diff)
    )

diffs.sort(
    key=lambda x: x[1]
)

for feature, diff in diffs:

    print(
        f"{feature:<20} {diff:.2f}"
    )