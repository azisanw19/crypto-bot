import json

def jsonFormat(object: json, sortKeys: bool = False) -> str:
    return json.dumps(object, sort_keys=sortKeys, indent=5)