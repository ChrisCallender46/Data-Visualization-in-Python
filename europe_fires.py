from pathlib import Path
import csv
import plotly.express as px

path = Path("../eq_data/europe_fire_data.csv")
lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract latitudes, longitudes, and brightness of fire
lats, lons, brightnesses = [], [], []
for row in reader:
    lat = float(row[0])
    lon = float(row[1])
    brightness = float(row[2])
    lats.append(lat)
    lons.append(lon)
    brightnesses.append(brightness)

title = "European Fires in the Past 24 Hours"
fig = px.scatter_geo(lat=lats, lon=lons, size=brightnesses, title=title,
                     color=brightnesses,
                     color_continuous_scale="turbo",
                     labels={"color": "Brightness"},
                     projection="natural earth",
                     scope="europe")
fig.show()