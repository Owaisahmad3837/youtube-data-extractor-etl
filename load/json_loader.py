import json
import os

os.makedirs("output", exist_ok=True)



def save_json(data):


    with open(
        "output/raw_data.json",
        "w",
        encoding="utf-8"

    ) as file:


        json.dump(
            data,
            file,
            indent=4
        )