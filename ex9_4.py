import requests
import os
from geojson import Feature, Point, FeatureCollection, dumps
import json


def main():
    resp = requests.get(
        "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=10.815898,106.695646&radius=2000&type={}&key={}".format(
            "bar", os.environ["GCP_API_KEY"]
        )
    )

    feartures = []
    for item in resp.json()["results"]:
        latitude = item["geometry"]["location"]["lat"]
        longitude = item["geometry"]["location"]["lng"]
        my_fearture = Feature(
            geometry=Point((longitude, latitude)),
            properties={"name": item["name"], "address": item["vicinity"]},
        )

        feartures.append(my_fearture)

    with open("pymi_bar.geojson", "w") as f:
        f.write(json.dumps(FeatureCollection(feartures)))


if __name__ == "__main__":
    main()
