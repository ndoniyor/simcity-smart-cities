import json
import sys

from utils.constants import Paths


def main():
    subject = sys.argv[1]
    data = {}
    with open(Paths.RAW_DATA_JSON / f"{subject}_part1.json", "r") as f:
        data = json.load(f)
        data = [x["attributes"] for x in data["features"]]

    with open(Paths.RAW_DATA_JSON / f"{subject}_part2.json", "r") as f:
        temp = json.load(f)
        data += [x["attributes"] for x in temp["features"]]

    mapping = {
        "Kings County": "3",
        "Queens County": "4",
        "Richmond County": "5",
        "New York County": "1",
        "Bronx County": "2",
    }

    import csv

    field_names = data[0].keys()

    with open(
        Paths.RAW_DATA_CSV / f"census_{subject}_data.csv", mode="w", newline=""
    ) as file:
        writer = csv.DictWriter(file, fieldnames=field_names)

        writer.writeheader()

        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    if sys.argv[0] == "1":
        print("ERR: No subject provided")
        sys.exit(1)
    main()
