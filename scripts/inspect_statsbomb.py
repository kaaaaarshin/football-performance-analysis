import json
import pandas as pd

with open("data/raw/competitions.json", "r") as f:
    competitions = json.load(f)

df = pd.DataFrame(competitions)

print(
    df[
        [
            "competition_id",
            "season_id",
            "competition_name",
            "season_name",
            "country_name"
        ]
    ]
)