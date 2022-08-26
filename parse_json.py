import json
from pathlib import Path

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