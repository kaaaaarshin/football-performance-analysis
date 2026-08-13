import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/player_profiles_clustered.csv"
)

player1 = "Sergio Ramos García"
player2 = "Aymeric Laporte"

features = [
    "passes",
    "pass_accuracy",
    "interceptions",
    "ball_recoveries",
    "duels",
    "blocks",
    "goals",
    "dribbles"
]

p1 = (
    df[df["player"] == player1]
    [features]
    .iloc[0]
)

p2 = (
    df[df["player"] == player2]
    [features]
    .iloc[0]
)

# normalize

temp = df[features]

p1 = p1 / temp.max()
p2 = p2 / temp.max()

angles = np.linspace(
    0,
    2 * np.pi,
    len(features),
    endpoint=False
).tolist()

angles += angles[:1]

p1 = p1.tolist()
p2 = p2.tolist()

p1 += p1[:1]
p2 += p2[:1]

fig = plt.figure(figsize=(8,8))
ax = plt.subplot(111, polar=True)

ax.plot(
    angles,
    p1,
    linewidth=2,
    label=player1
)

ax.fill(
    angles,
    p1,
    alpha=0.25
)

ax.plot(
    angles,
    p2,
    linewidth=2,
    label=player2
)

ax.fill(
    angles,
    p2,
    alpha=0.25
)

ax.set_xticks(
    angles[:-1]
)

ax.set_xticklabels(
    features
)

plt.legend(
    loc="upper right"
)

plt.title(
    f"{player1} vs {player2}"
)

plt.show()