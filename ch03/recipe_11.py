import csv
from pathlib import Path
from math import radians, sin, cos, sqrt, asin
from functools import partial

MI = 3959
NM = 3440
KM = 6373

def haversine(
        lat_1: float, lon_1: float,
        lat_2: float, lon_2: float, *, R: float
) -> float:
    """Distance between points.
    R is Earth's radius.
    R=MI computes in miles. Default is nautical miles.

    >>> round(haversine(36.12, -86.67, 33.94, -118.40, R=6372.8), 5)
    2887.25995
    """
    delta_lat = radians(lat_2) - radians(lat_1)
    delta_lon = radians(lon_2) - radians(lon_1)
    lat_1 = radians(lat_1)
    lat_2 = radians(lat_2)
    a = sqrt(
        sin(delta_lat / 2) ** 2 + 
        cos(lat_1) * cos(lat_2) * sin(delta_lon / 2) ** 2
    )
    return R * 2 * asin(a)

nm_haversine = partial(haversine, R=NM)

source_path = Path("data/waypoints.csv")
with source_path.open() as source_file:
    reader = csv.DictReader(source_file)
    start = next(reader)
    for point in reader:
        d = nm_haversine(
            float(start['lat']),
            float(start['lon']),
            float(point['lat']),
            float(point['lon'])
        )
        print(start, point, d)
        start = point

def distances_draft():
    source_path = Path("data/waypoints.csv")
    with source_path.open() as source_file:
        reader = csv.DictReader(source_file)
        start = next(reader)
        for point in reader:
            d = nm_haversine(
                float(start['lat']),
                float(start['lon']),
                float(point['lat']),
                float(point['lon'])
            )
            print(start, point, d)
            start = point

def distances(
        source_path: Path = Path("data/waypoints.csv")
) -> None:
    ...

if __name__ == "__main__":
    distances()