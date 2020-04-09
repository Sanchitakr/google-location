import json
import simplekml

def iterateData(data):
    for point in data:
        ts = int(point["timestampMs"])
        lat = int(point["latitudeE7"]) / 10000000
        long = int(point["longitudeE7"]) / 10000000
        yield(ts, (lat, long))

print("Parsing...")

data = json.load(open("Location History.json", "r"))

data = data['locations']

print("There are %d data points" % len(data))

fCount = 0
i = 0

kml = None
pieces = []

for timestamp, (lat, long) in iterateData(data):
      if i % 190000 == 0 and i != 0 and False:
            kml = simplekml.Kml()
            kml.newlinestring(name="line", coords=pieces)
            kml.save(f"output{fCount}.kml")
            pieces = []
            fCount += 1
      pieces.append((long,lat))
      i += 1

if len(pieces) > 0:
        kml = simplekml.Kml()
        kml.newlinestring(name="line", coords=pieces)
        kml.save(f"output{fCount}.kml")
