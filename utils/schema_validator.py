import json
from jsonschema import validate

def load_schema(schema_file):
    with open(schema_file, 'r') as file:
        return json.load(file)

def validate_response(response_json, schema_file):
    schema = load_schema(schema_file)
    validate(instance=response_json, schema=schema)

