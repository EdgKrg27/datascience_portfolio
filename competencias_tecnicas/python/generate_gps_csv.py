import csv
import random
from datetime import datetime, timedelta

NUM_RECORDS = 1000000
NUM_VEHICLE = 1000
START_TIME = datetime(2024, 1, 1, 0, 0, 0)

LAT_MIN, LAT_MAX = 19.25, 19.55
LON_MIN, LON_MAX = -99.30, -99.00

vehicle_ids = [f"vehicle{str(i).zfill(3)}" for i in range(1, NUM_VEHICLE + 1)]


def generate_random_row():
    vehicle_id = random.choice(vehicle_ids)
    random_min = random.randint(0, 60 * 24 * 30)
    timestamp = (START_TIME + timedelta(minutes=random_min)).isoformat()
    latitude = round(random.uniform(LAT_MIN, LAT_MAX), 6)
    longitude = round(random.uniform(LON_MIN, LON_MAX), 6)
    return [vehicle_id, timestamp, latitude, longitude]


csv_path = "vehicle_cdmx.csv"

with open(csv_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["vehicle_id", "timestamp", "latitude", "logitude"])
    for _ in range(NUM_RECORDS):
        writer.writerow(generate_random_row())

csv_path
