import json
import os
from re import match

from jsonschema import validate, RefResolver, exceptions


def get_example_json(filename, res) -> dict:
    """
    Gets example json for a request. The json is validated.
    :param filename: the name of the request, also source of the json schema for validation
    :param res: DbApiDocRes, resources, the dummy data
    :return: the json in a dict
    """
    SCHEMAS_REL_PATH = "../json_schema"

    f = filename.split(".")[0]
    example_json = res.get_value_from_dict(f)
    with open("%s/%s" % (SCHEMAS_REL_PATH, filename)) as schema:
        j_schema = json.load(schema)
    schemas_path = 'file:///{0}/{1}/'.format(os.getcwd().replace("\\", "/"), SCHEMAS_REL_PATH)

    j_resolver = RefResolver(schemas_path, j_schema)
    try:
        validate(example_json, j_schema, resolver=j_resolver)
    except exceptions.ValidationError as e:
        raise Exception(
            "Mock data for {} is incorrect or out-of-date.\nThe problem: {}\nGiven example json: {}".format(filename,
                                                                                                            e.message,
                                                                                                            example_json))

    return example_json


# from pprint import pprint
# example_json = get_example_json('get_all_rooms_logs.json')
# pprint(example_json)

def extract_schemas(var, key="$ref", schema_v="$schema") -> None:
    """
    Recursively extracts all nested shemas in place. Modified from https://stackoverflow.com/a/29652561
    :param var: a dictionary with the data
    :param key: which keys from the dictionary are to be replaced
    :param schema_v: the new json schema (as a dict)
    :return:
    """
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                schema = match("file:(\w*)\.json", v).group(1)
                var[schema] = get_schema(schema)
                extract_schemas(var[schema], key)
                del var[key]
            if isinstance(v, dict):
                extract_schemas(v, key)
            elif isinstance(v, list):
                for d in v:
                    extract_schemas(d, key)


def get_schema(schema_name) -> json:
    """
    Gets json schema extracted to full depth as a dictionary.
    :param schema_name: the name of the schema, as a string
    :return: dict
    """
    SCHEMA_DIR = "../json_schema"
    with open("%s/%s.json" % (SCHEMA_DIR, schema_name)) as schema_f:
        schema = json.load(schema_f)
    extract_schemas(schema)
    return schema
