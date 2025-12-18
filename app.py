from flask import Flask, jsonify
import requests
import csv
import os

app = Flask(__name__)

API_URL = "https://rickandmortyapi.com/api/character"
CSV_FILE = "characters.csv"


def fetch_characters():
    results = []
    page = 1

    while True:
        response = requests.get(API_URL, params={"page": page})
        data = response.json()

        for char in data["results"]:
            if (
                char["species"] == "Human"
                and char["status"] == "Alive"
                and "Earth" in char["origin"]["name"]
            ):
                results.append({
                    "name": char["name"],
                    "location": char["location"]["name"],
                    "image": char["image"]
                })

        if not data["info"]["next"]:
            break
        page += 1

    return results


def write_csv(characters):
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["name", "location", "image"]
        )
        writer.writeheader()
        writer.writerows(characters)


@app.route("/characters", methods=["GET"])
def get_characters():
    characters = fetch_characters()
    write_csv(characters)
    return jsonify(characters)


@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

