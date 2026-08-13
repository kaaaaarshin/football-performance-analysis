import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/player_roles.csv"
)

features = df.drop(
    columns=["player", "cluster", "role"]
)

scaler = StandardScaler()

X = scaler.fit_transform(features)

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X)

plt.figure(figsize=(10, 7))

scatter = plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=df["cluster"],
)

plt.title("Player Clusters")

plt.xlabel("PCA 1")
plt.ylabel("PCA 2")

from sklearn.metrics import silhouette_score

score = silhouette_score(
    X_scaled,
    kmeans.labels_
)

print(score)

plt.show()