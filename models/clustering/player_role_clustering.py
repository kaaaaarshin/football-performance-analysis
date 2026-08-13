import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# ==========================
# LOAD DATA
# ==========================

df = pd.read_csv(
    "data/processed/player_profiles.csv"
)

# Keep player names
players = df["player"]

# Features only
X = df.drop(columns=["player"])

# ==========================
# SCALE FEATURES
# ==========================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("Scaled Shape:")
print(X_scaled.shape)

# ==========================
# KMEANS CLUSTERING
# ==========================

print("\nKMEANS")

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)

# ==========================
# EVALUATION
# ==========================

score = silhouette_score(
    X_scaled,
    clusters
)

print("\nSilhouette Score:")
print(score)

# ==========================
# ASSIGN CLUSTERS
# ==========================

df["cluster"] = clusters

# TEMPORARY ROLE MAPPING
# We will verify after checking cluster summary

role_mapping = {
    0: "Defender",
    1: "Midfielder",
    2: "Attacker",
    3: "Goalkeeper",
    4: "Utility"
}

df["role"] = df["cluster"].map(role_mapping)

# ==========================
# RESULTS
# ==========================

print("\nCluster Counts:")

print(
    df["cluster"]
    .value_counts()
    .sort_index()
)

print("\nSample Players:")

print(
    df[
        ["player", "cluster", "role"]
    ]
    .head(30)
)

# ==========================
# CLUSTER SUMMARY
# ==========================

pd.set_option("display.max_columns", None)

cluster_summary = (
    df.groupby("cluster")
      .mean(numeric_only=True)
      .round(2)
)

print("\nCLUSTER SUMMARY")
print(cluster_summary)

cluster_summary.to_csv(
    "data/processed/cluster_summary.csv",
    index=True
)

# ==========================
# SAMPLE PLAYERS PER CLUSTER
# ==========================

for c in sorted(df["cluster"].unique()):

    print("\n" + "=" * 50)
    print(f"CLUSTER {c}")
    print("=" * 50)

    print(
        df[df["cluster"] == c]
        [["player"]]
        .head(30)
    )

# ==========================
# SAVE OUTPUT
# ==========================

df.to_csv(
    "data/processed/player_profiles_clustered.csv",
    index=False
)

print(
    "\nSaved: data/processed/player_profiles_clustered.csv"
)

print("\nRole Counts:")
print(
    df["role"].value_counts()
)