# src/parse_framedata.py

import json
import os
import pandas as pd

def parse_revised_move_data(character, move_name, move_data):
    if not move_data or "totalFrames" not in move_data:
        return None

    total = move_data.get("totalFrames")
    iasa = move_data.get("iasa")
    hitframes = move_data.get("hitFrames", [])
    startup = min((hf["start"] for hf in hitframes), default=None)
    active = [(hf["start"], hf["end"]) for hf in hitframes]
    hitboxes = move_data.get("hitboxes", [])
    damages = [hb.get("damage", 0) for hb in hitboxes]
    max_damage = max(damages) if damages else None
    multi_hit = len(hitframes) > 1

    return {
        "character": character,
        "move_name": move_name,
        "startup": startup,
        "active_windows": active,
        "multi_hit": multi_hit,
        "damage_max": max_damage,
        "iasa": iasa,
        "total_frames": total
    }

def parse_all_characters(framedata_dir):
    all_moves = []
    for filename in os.listdir(framedata_dir):
        if not filename.endswith(".json"):
            continue
        character_name = filename.replace(".framedata.json", "")
        filepath = os.path.join(framedata_dir, filename)
        with open(filepath, 'r') as f:
            data = json.load(f)
        for move_name, move_data in data.items():
            if move_name.startswith("0x"):
                continue
            parsed = parse_revised_move_data(character_name, move_name, move_data)
            if parsed:
                all_moves.append(parsed)
    return pd.DataFrame(all_moves)

if __name__ == "__main__":
    framedata_dir = "data/raw"
    output_path = "data/move_summary.csv"
    df = parse_all_characters(framedata_dir)
    df.to_csv(output_path, index=False)
    print(f"Parsed {len(df)} moves and saved to {output_path}")
