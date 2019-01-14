class DbApiDocRes:
    cats = {}
    jsonFile_to_dict = {}

    def __init__(self):
        # List of all methods
        self.cats = {"read_objects": {
            "get_all_rooms": {
                "status": "DESIGNED",
                "request": "GET",
                "params": [],
            },
            "get_bldg_by_name": {
                "status": "DESIGNED",
                "request": "GET",
                "params": ["String name", ],
            },
            "get_room_by_name": {
                "status": "DESIGNED",
                "request": "GET",
                "params": ["String name", ],
            },
            "get_rooms_by_bldg": {
                "status": "DESIGNED",
                "request": "GET",
                "params": ["String bldg_id", ],
            },
            "get_sensors_in_room": {
                "status": "DESIGNED",
                "request": "GET",
                "params": ["String room_id", ],
            },
        }, "read_senslogs": {
            "get_all_rooms_logs": {
                "status": "DESIGNED",
                "request": "GET",
                "params": ["long start_millis", "long end_millis", ],
            },
            "get_room_logs": {
                "status": "DESIGNED",
                "request": "GET",
                "params": ["String room_id", "long startMillis", "long endMillis", ],
            },
        }, "read_ctrllogs": {
            "get_ctrllogs": {
                "status": "UNDESIGNED"
            },
        }, "control_update": {
            "update_bldg": {
                "status": "DESIGNED",
                "request": "POST",
            },
            "update_room": {
                "status": "DESIGNED",
                "request": "POST",
            },
            "update_sensor": {
                "status": "DESIGNED",
                "request": "POST",
            },
        }, "control_remove": {
            "remove_bldg": {
                "status": "UNDESIGNED"
            },
            "remove_room": {
                "status": "UNDESIGNED"
            },
            "remove_sensor": {
                "status": "UNDESIGNED"
            },
        }, "control_sampling": {
            "set_sampling_f": {
                "status": "UNDESIGNED"
            },
        }, "control_controllers": {
        }, "write_add": {
            "add_bldg": {
                "status": "DESIGNED",
                "request": "POST",
                "response": ["bldg_id"]
            },
            "add_room": {
                "status": "DESIGNED",
                "request": "POST",
                "response": ["room_id"]
            },
            "add_sensor": {
                "status": "DESIGNED",
                "request": "POST",
                "response": ["sensor_id"]
            },

        }, "write_log": {
            "save_log": {
                "status": "DESIGNED",
                "request": "POST",
            },
            "save_logs": {
                "status": "DESIGNED",
                "request": "POST",
            },
        }, "authentication": {}}

        # Dummy data for example jsons
        self.jsonFile_to_dict["room"] = {
            "id": ["b02r01", "b01r02", "b03r03"],
            "name": ["Lab012", "Lab090", "Lab876"],
            "Description": ["Physics lab on second floor of KELVIN building",
                            "Physics lab on fourth floor of RANKIN building",
                            "Physics lab on first floor of JAMES WATT SOUTH building"],
            "bldg_id": ["b01", "b02", "b03"]}

        room = self.jsonFile_to_dict["room"]

        self.jsonFile_to_dict["sensor"] = {
            "id": ["b02r01s01", "b01r02s02", "b03r03s03"],
            "name": ["sensor1", "sensor2", "sensor3"],
            "Description": ["Relative humidity sensor", "Thermometer/humidity sensor", "Light dependent resistor"],
            "room_id": [room["id"][0], room["id"][1], room["id"][2]],
            "unit": ["KELVIN", "PERCENT", "VOLTS"]
        }

        sensor = self.jsonFile_to_dict["sensor"]

        self.jsonFile_to_dict["bldg"] = {
            "id": ["b02", "b01", "b03"],
            "name": ["KELVIN bldg", "RANKIN bldg", "BOYD ORR bldg"],
            "Description": ["Main bldg of physics department", "Main lab bldg of Engineering department",
                            "Main bldg of Engineering department"]
        }

        bldg = self.jsonFile_to_dict["bldg"]

        self.jsonFile_to_dict["get_all_rooms"] = {
            "rooms": [[self.get_value_from_dict("room", 0), self.get_value_from_dict("room", 1),
                       self.get_value_from_dict("room", 2)],
                      [self.get_value_from_dict("room", 0), self.get_value_from_dict("room", 1)],
                      [self.get_value_from_dict("room", 2)]]
        }

        self.jsonFile_to_dict["log"] = {
            "timestamp": [54, 65, 89],
            "value": [79.878, 17.001, 45.124]
        }
        log = self.jsonFile_to_dict["log"]

        self.jsonFile_to_dict["sensor_logs"] = {
            "sensor_id": [sensor["id"][0], sensor["id"][1], sensor["id"][2]],
            "unit": [sensor["unit"][0], sensor["unit"][1], sensor["unit"][2]],
            "logs": [[self.get_value_from_dict("log", 0), self.get_value_from_dict("log", 1)],
                     [self.get_value_from_dict("log", 2), self.get_value_from_dict("log", 1)],
                     [self.get_value_from_dict("log", 0), self.get_value_from_dict("log", 2)]]
            # "logs" : [[300, 267, 343], [37, 65, 91], [0.005, 1.223, 0.529]]
        }

        sensor_logs = self.jsonFile_to_dict["sensor_logs"]

        self.jsonFile_to_dict["room_logs"] = {
            "room_id": [room["id"][0], room["id"][1], room["id"][2]],
            "sensor_logs": [[self.get_value_from_dict("sensor_logs", 0),
                             self.get_value_from_dict("sensor_logs", 1)],
                            [self.get_value_from_dict("sensor_logs", 2),
                             self.get_value_from_dict("sensor_logs", 1)],
                            [self.get_value_from_dict("sensor_logs", 0),
                             self.get_value_from_dict("sensor_logs", 2)]]

        }

        room_logs = self.jsonFile_to_dict["room_logs"]

        self.jsonFile_to_dict["get_room_logs"] = {
            "room_id": [room["id"][0], room["id"][1], room["id"][2]],
            "start_millis": [100, 50, 150],
            "end_millis": [110, 150, 175],
            "room_logs": [self.get_value_from_dict("room_logs", 0), self.get_value_from_dict("room_logs", 1),
                          self.get_value_from_dict("room_logs", 2)]
        }

        self.jsonFile_to_dict["get_all_rooms_logs"] = {
            "start_millis": [100, 50, 150],
            "end_millis": [110, 150, 175],
            "rooms_logs": [[self.get_value_from_dict("room_logs", 0),
                            self.get_value_from_dict("room_logs", 1)],
                           [self.get_value_from_dict("room_logs", 0),
                            self.get_value_from_dict("room_logs", 2)],
                           [self.get_value_from_dict("room_logs", 1),
                            self.get_value_from_dict("room_logs", 2)]]
        }

        self.jsonFile_to_dict["get_sensors_in_room"] = {
            "room_id": [room["id"][0], room["id"][1], room["id"][2]],
            "sensors": [[self.get_value_from_dict("sensor", 0),
                         self.get_value_from_dict("sensor", 1)],
                        [self.get_value_from_dict("sensor", 2),
                         self.get_value_from_dict("sensor", 0)],
                        [self.get_value_from_dict("sensor", 2),
                         self.get_value_from_dict("sensor", 1)]]
        }

        self.jsonFile_to_dict["get_bldg_by_name"] = {
            "bldg": [self.get_value_from_dict("bldg", 0),
                     self.get_value_from_dict("bldg", 1),
                     self.get_value_from_dict("bldg", 2)]
        }

        self.jsonFile_to_dict["get_rooms_by_bldg"] = {
            "rooms": [[self.get_value_from_dict("room", 0)],
                      [self.get_value_from_dict("room", 1)],
                      [self.get_value_from_dict("room", 2)]]
        }

        self.jsonFile_to_dict["get_room_by_name"] = {
            "room": [self.get_value_from_dict("room", 0),
                     self.get_value_from_dict("room", 1),
                     self.get_value_from_dict("room", 2)]
        }

        self.jsonFile_to_dict["update_bldg"] = {
            "id": bldg["id"],
            "name": ["JAMES MATT building", "", "JUST NEW NAME bldg"],
            "description": ["New building for physics department.", "Only a new description of the building.", ""]
        }

        self.jsonFile_to_dict["update_room"] = {
            "id": room["id"],
            "name": ["Lab007", "UpdatedNameRoom", ""],
            "description": ["A new top secret lab", "", "Just a new description."]
        }

        self.jsonFile_to_dict["update_sensor"] = {
            "id": sensor["id"],
            "name": ["AwesomenessSensor", "sensor4", ""],
            "description": ["A sensor measuring the present awesomeness", "", "Just a new description."],
            "unit": ["percents of BoydOrr", "CELSIUS", ""]
        }

        self.jsonFile_to_dict["add_bldg"] = {
            "name": ["KELVIN bldg", "RANKIN bldg", "BOYD ORR bldg"],
            "description": ["Main bldg of physics department", "Main lab bldg of Engineering department",
                            "Main bldg of Engineering department"]
        }

        self.jsonFile_to_dict["add_room"] = {
            "name": ["Lab017", "Lab050", "Lab734"],
            "description": ["Physics lab on first floor of KELVIN building",
                            "Physics lab on third floor of RANKINE building",
                            "Physics lab on second floor of JAMES WATT SOUTH building"]
        }

        self.jsonFile_to_dict["add_sensor"] = {
            "name": ["sensor1", "sensor2", "sensor3"],
            "Description": ["Relative humidity sensor", "Thermometer/humidity sensor", "Light dependent resistor"],
            "room_id": [room["id"][0], room["id"][1], room["id"][2]],
            "unit": ["KELVIN", "PERCENT", "VOLTS"]
        }

        self.jsonFile_to_dict["save_log"] = {
            "sensor_id": [sensor["id"][0], sensor["id"][1], sensor["id"][2]],
            "log": [self.get_value_from_dict("log", 0),
                    self.get_value_from_dict("log", 1),
                    self.get_value_from_dict("log", 2)]
        }

        self.jsonFile_to_dict["save_logs"] = {
            "logs": [[self.get_value_from_dict("save_log", 0),
                      self.get_value_from_dict("save_log", 1)],
                     [self.get_value_from_dict("save_log", 2),
                      self.get_value_from_dict("save_log", 0)],
                     [self.get_value_from_dict("save_log", 2),
                      self.get_value_from_dict("sensor", 1)]]
        }

    def get_value_from_dict(self, filename, i=0):
        exp_json = {}
        if filename not in self.jsonFile_to_dict:
            raise Exception("There is no mock data for %s" % filename)
        json_dict = self.jsonFile_to_dict[filename]
        for item in json_dict:
            exp_json.update({item: json_dict[item][i]})

        return exp_json
