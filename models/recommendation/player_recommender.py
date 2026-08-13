import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_csv(
    "data/processed/player_profiles_clustered.csv"
)

# Features used for similarity
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

# Scale
scaler = MinMaxScaler()
X = scaler.fit_transform(df[features])

# Similarity matrix
sim_matrix = cosine_similarity(X)

player_name = "Sergio Ramos García"

# Find player index
player_idx = df[df["player"] == player_name].index[0]

# Similarities
scores = list(enumerate(sim_matrix[player_idx]))

# Remove self
scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:]

print("\nMost Similar To", player_name)
print("-" * 50)

for idx, score in scores[:10]:
    print(
        f"{df.loc[idx,'player']} "
        f"({score*100:.2f}%) "
        f"[{df.loc[idx,'role']}]"
    )

