import json
from pathlib import Path
import jsonschema
from jsonschema import validate

configSchema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "version": {"type": "number"},
        "path": {"type": "string"},
    },
    "required": ["name", "version"]
}

def parse_json(filepath):
  if not Path(filepath).is_file():
    # also can throw file not exist
    return (False, "file not exist")

  with open(filepath, "r") as file:
    content = file.read()
    if not is_json(content):
      return (False, "No valid json")
    
    return (True, json.loads(content))

def is_json(file):
  try:
    json.loads(file)
  except Exception as e:
    print(e)
    return False
  return True

def validateSchema(jsonData):
    try:
        validate(instance=jsonData, schema=configSchema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        return False
    return True

(success, value) = parse_json("assets/not_existing.json")
print(success)
print(value)

(success, value) = parse_json("assets/empty.json")
print(success)
print(value)

(success, value) = parse_json("assets/invalid.json")
print(success)
print(value)

(success, value) = parse_json("assets/valid.json")
print(success)
print(value)

print("##### VALIDATE SCHEMA #####")

jsonData = json.loads('{"name": "config1", "number": 1, "path": "72"}')
isValid = validateSchema(jsonData)
print(isValid)

jsonData = json.loads('{"name": "config2", "version": "2", "path": 72}')
isValid = validateSchema(jsonData)
print(isValid)

jsonData = json.loads('{"name": "config2", "version": 3, "path": "pathToFile"}')
isValid = validateSchema(jsonData)
print(isValid)

jsonData = json.loads('{"name": "config2", "version": 3}')
isValid = validateSchema(jsonData)
print(isValid)
