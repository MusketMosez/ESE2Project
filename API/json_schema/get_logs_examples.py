"""
Example response JSONs and their validation for Read Database API - reading logs
"""

import json
from jsonschema import validate, RefResolver
import os
from pprint import pprint

VERBOSE = True  # change to False to get rid of print outs

# Init JSONs
log1 = {
    "timestamp": 101,  # normal values will be around 10e12, this hre is for readability
    "value": 314.15
}
log2 = {
    "timestamp": 102,
    "value": 315.00
}
log3 = {
    "timestamp": 103,
    "value": 42.47
}
log4 = {
    "timestamp": 999,  # after end, see get_room_logs below
    "value": 50.00
}
sensor_logs_1 = {
    "sensor_id": "b01r01s01",
    "unit": "KELVIN",
    "logs": [
        log1,
        log2
    ]
}
sensor_logs_2 = {
    "sensor_id": "b01r01s01",
    "unit": "PERCENT",
    "logs": [
        log3
    ]
}
room_logs_1 = {
    "room_id": "b01r01",
    "sensor_logs": [
        sensor_logs_1,
        sensor_logs_2
    ]
}
room_logs_2 = {
    "room_id": "b01r02",
    "sensor_logs": []  # no data so far
}

get_room_logs = {
    "room_id": "b01r01",
    "start_millis": 100,
    "end_millis": 110,
    "room_logs": room_logs_1
}
get_all_rooms_logs = {
    "start_millis": 50,
    "end_millis": 150,
    "rooms_logs": [
        room_logs_1,
        room_logs_2
    ]
}

if VERBOSE:
    print("example get_all_rooms_logs response")
    pprint(get_all_rooms_logs)
    print()
    print("example get_room_logs response")
    pprint(get_room_logs)
    print()

# Load schemas
with open("log.json") as log_schema_f:
    log_schema = json.load(log_schema_f)
with open("sensor_logs.json") as sensor_logs_schema_f:
    sensor_logs_schema = json.load(sensor_logs_schema_f)
with open("room_logs.json") as room_logs_schema_f:
    room_logs_schema = json.load(room_logs_schema_f)

with open("get_room_logs.json") as get_room_logs_schema_f:
    get_room_logs_schema = json.load(get_room_logs_schema_f)
with open("get_all_rooms_logs.json") as get_all_rooms_logs_schema_f:
    get_all_rooms_logs_schema = json.load(get_all_rooms_logs_schema_f)

# Init resolvers to correctly link more nested jsons
schemas_path = 'file:///{0}/'.format(os.getcwd().replace("\\", "/"))
sensor_logs_resolver = RefResolver(schemas_path, sensor_logs_schema)
room_logs_resolver = RefResolver(schemas_path, room_logs_schema)
get_room_logs_resolver = RefResolver(schemas_path, get_room_logs_schema)
get_all_rooms_logs_resolver = RefResolver(schemas_path, get_all_rooms_logs_schema)

# Validate, should not throw
validate(log1, log_schema)
validate(log2, log_schema)
validate(log3, log_schema)
validate(log4, log_schema)
validate(sensor_logs_1, sensor_logs_schema, resolver=sensor_logs_resolver)
validate(sensor_logs_2, sensor_logs_schema, resolver=sensor_logs_resolver)
validate(room_logs_1, room_logs_schema, resolver=room_logs_resolver)
validate(room_logs_2, room_logs_schema, resolver=room_logs_resolver)

validate(get_room_logs, get_room_logs_schema, resolver=get_room_logs_resolver)
validate(get_all_rooms_logs, get_all_rooms_logs_schema, resolver=get_all_rooms_logs_resolver)

if VERBOSE:
    print("Validation successful!")
