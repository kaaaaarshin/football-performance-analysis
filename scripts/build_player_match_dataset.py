import requests
import pandas as pd


def extract_match_stats(match_id):

    url = f"https://raw.githubusercontent.com/statsbomb/open-data/master/data/events/{match_id}.json"

    events = requests.get(url).json()

    player_stats = {}

    for event in events:

        if "player" not in event:
            continue

        player = event["player"]["name"]

        if player not in player_stats:

            player_stats[player] = {
                "passes": 0,
                "successful_passes": 0,
                "shots": 0,
                "goals": 0,
                "dribbles": 0,
                "pressures": 0,
                "interceptions": 0,
                "ball_recoveries": 0,
                "duels": 0,
                "blocks": 0,
                "fouls_won": 0,
                "fouls_committed": 0
            }

        event_type = event["type"]["name"]

        if event_type == "Pass":

            player_stats[player]["passes"] += 1

            if "pass" in event and "outcome" not in event["pass"]:
                player_stats[player]["successful_passes"] += 1

        elif event_type == "Shot":

            player_stats[player]["shots"] += 1

            if (
                "shot" in event
                and "outcome" in event["shot"]
                and event["shot"]["outcome"]["name"] == "Goal"
            ):
                player_stats[player]["goals"] += 1

        elif event_type == "Dribble":
            player_stats[player]["dribbles"] += 1

        elif event_type == "Pressure":
            player_stats[player]["pressures"] += 1
        
        elif event_type == "Interception":
            player_stats[player]["interceptions"] += 1

        elif event_type == "Ball Recovery":
            player_stats[player]["ball_recoveries"] += 1

        elif event_type == "Duel":
            player_stats[player]["duels"] += 1

        elif event_type == "Block":
            player_stats[player]["blocks"] += 1

        elif event_type == "Foul Won":
            player_stats[player]["fouls_won"] += 1

        elif event_type == "Foul Committed":
            player_stats[player]["fouls_committed"] += 1

    rows = []

    for player, stats in player_stats.items():

        pass_accuracy = 0

        if stats["passes"] > 0:
            pass_accuracy = (
                stats["successful_passes"]
                / stats["passes"]
            ) * 100

        row = {
            "match_id": match_id,
            "player": player,
            "passes": stats["passes"],
            "successful_passes": stats["successful_passes"],
            "pass_accuracy": round(pass_accuracy, 2),
            "shots": stats["shots"],
            "goals": stats["goals"],
            "dribbles": stats["dribbles"],
            "pressures": stats["pressures"],
            "interceptions": stats["interceptions"],
            "ball_recoveries": stats["ball_recoveries"],
            "duels": stats["duels"],
            "blocks": stats["blocks"],
            "fouls_won": stats["fouls_won"],
            "fouls_committed": stats["fouls_committed"]
            }

        rows.append(row)

    return rows


# ==========================
# MAIN
# ==========================

matches_df = pd.read_csv(
    "data/raw/laliga_2015_16_matches.csv"
)

match_ids = matches_df["match_id"].tolist()

print(f"Total matches found: {len(match_ids)}")

# TEST MODE

all_rows = []

for i, match_id in enumerate(match_ids, start=1):

    print(
        f"[{i}/{len(match_ids)}] Processing Match ID: {match_id}"
    )

    rows = extract_match_stats(match_id)

    all_rows.extend(rows)

dataset = pd.DataFrame(all_rows)

print("\nDataset Shape:")
print(dataset.shape)

print("\nSample Data:")
print(dataset.head())

dataset.to_csv(
    "data/processed/player_match_dataset.csv",
    index=False
)

print(
    "\nSaved: data/processed/player_match_dataset.csv"
)

print(dataset.info())
print(dataset.isnull().sum())