import pandas as pd
import folium


class Map:
    "A Wrapper for leaflet-map related objects"

    def __init__(
        self,
        defaultLocation=[27.618902, 85.537709],
        htmlLocation="./folium_map/map.html",
    ):
        self.htmlLocation = htmlLocation
        # load co-ordinate data
        self.map_cols = ["id", "name", "north", "east", "emptySpots"]
        self.locationsData = pd.read_csv(
            "./folium_map/parking_lots.csv", header=None, names=self.map_cols
        )
        self.map = folium.Map(location=defaultLocation, zoom_start=18)

    def update_location(self, location, zoom_start=18):
        self.map = folium.Map(location=location, zoom_start=zoom_start)

    def generate(self, msg="Available Spots: "):
        for locData in self.locationsData.itertuples():
            folium.Marker(
                [locData.north, locData.east],
                popup=(msg + str(locData.emptySpots)),
                tooltip=locData.name,
                icon=folium.Icon(prefix="fa", icon="car", color="red"),
            ).add_to(self.map)
        self.map.save("./folium_map/map.html")