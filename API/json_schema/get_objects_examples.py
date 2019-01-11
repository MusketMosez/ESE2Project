"""
Example response JSONs and their validation for Read Database API - reading info about sensors, rooms and buildings
"""

import json
from jsonschema import validate
from pprint import pprint

VERBOSE = True  # change to False to get rid of print outs

# Init JSONs
sensor1 = {
    "id": "b01r01s01",
    "name": "DHT11",
    "description": "Thermometer measuring the room temperature in lab 007",
    "room_id": "b01r01",
    "unit": "KELVIN"
}
sensor2 = {
    "id": "b01r01s02",
    "name": "DHT11",
    "description": "Relative humidity sensor",
    "room_id": "b01r01",
    "unit": "PERCENT"
}
room1 = {
    "id": "b01r01",
    "name": "Lab007",
    "description": "Physics lab 007 on the ground floor in Kelvin bldg",
    "bldg_id": "b01",
}
room2 = {
    "id": "b01r01",
    "name": "Lab101",
    "description": "Physics lab 101 on the first floor in Kelvin bldg",
    "bldg_id": "b01",
}
bldg = {
    "id": "b01",
    "name": "Kelvin bldg",
    "description": "Main bldg of the Physics department",
}

get_all_rooms = {"rooms": [room1, room2]}
get_bldg_by_name = {"bldg": bldg}
get_room_by_name = {"room": room1}
get_rooms_by_bldg = {"rooms": [room1, room2]}
get_sensors_in_room = {
    "room_id": "b01r01",
    "sensors": [sensor1, sensor2]
}

if VERBOSE:
    print("example get_all_rooms response")
    pprint(get_all_rooms)
    print()
    print("example get_bldg_by_name response")
    pprint(get_bldg_by_name)
    print()
    print("example get_room_by_name response")
    pprint(get_room_by_name)
    print()
    print("example get_rooms_by_bldg response")
    pprint(get_rooms_by_bldg)
    print()
    print("example get_sensors_in_room response")
    pprint(get_sensors_in_room)
    print()

# Load schemas
with open("sensor.json") as sensor_schema_f:
    sensor_schema = json.load(sensor_schema_f)
with open("room.json") as room_schema_f:
    room_schema = json.load(room_schema_f)
with open("bldg.json") as bldg_schema_f:
    bldg_schema = json.load(bldg_schema_f)

with open("get_all_rooms.json") as get_all_rooms_schema_f:
    get_all_rooms_schema = json.load(get_all_rooms_schema_f)
with open("get_bldg_by_name.json") as get_bldg_by_name_schema_f:
    get_bldg_by_name_schema = json.load(get_bldg_by_name_schema_f)
with open("get_room_by_name.json") as get_room_by_name_schema_f:
    get_room_by_name_schema = json.load(get_room_by_name_schema_f)
with open("get_rooms_by_bldg.json") as get_rooms_by_bldg_schema_f:
    get_rooms_by_bldg_schema = json.load(get_rooms_by_bldg_schema_f)
with open("get_sensors_in_room.json") as get_sensors_in_room_schema_f:
    get_sensors_in_room_schema = json.load(get_sensors_in_room_schema_f)

# Validate, should not throw
validate(sensor1, sensor_schema)
validate(sensor2, sensor_schema)
validate(room1, room_schema)
validate(room2, room_schema)
validate(bldg, bldg_schema)

validate(get_all_rooms, get_all_rooms_schema)
validate(get_bldg_by_name, get_bldg_by_name_schema)
validate(get_room_by_name, get_room_by_name_schema)
validate(get_rooms_by_bldg, get_rooms_by_bldg_schema)
validate(get_sensors_in_room, get_sensors_in_room_schema)

if VERBOSE:
    print("Validation successful!")
