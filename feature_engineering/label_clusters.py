import pandas as pd

df = pd.read_csv(
    "data/processed/player_profiles_clustered.csv"
)

print(df.head())

print(
    df["cluster"].value_counts()
)

for cluster in sorted(df["cluster"].unique()):

    print("\n")
    print("=" * 50)
    print(f"CLUSTER {cluster}")
    print("=" * 50)

    print(
        df[df["cluster"] == cluster]
        [["player"]]
        .head(50)
    )

stars = [
    "Cristiano Ronaldo dos Santos Aveiro",
    "Lionel Andrés Messi Cuccittini",
    "Neymar da Silva Santos Junior",
    "Luka Modrić",
    "Sergio Ramos García",
    "Jan Oblak"
]

for star in stars:

    player = df[
        df["player"] == star
    ]

    print(player[
        ["player", "cluster"]
    ])

role_map = {
    0: "Defender",
    1: "Midfielder",
    2: "Attacker",
    3: "Goalkeeper",
    4: "Utility"
}

df["role"] = (
    df["cluster"]
    .map(role_map)
)

df.to_csv(
    "data/processed/player_roles.csv",
    index=False
)

print(
    "Saved: data/processed/player_roles.csv"
)

print(
    df[["player", "cluster", "role"]]
    .sample(20)
)

df.to_csv(
    "data/processed/player_roles.csv",
    index=False
)

print(
    df["role"].value_counts()
)