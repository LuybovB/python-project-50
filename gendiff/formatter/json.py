import json


def format_json(different: dict) -> str:
    return json.dumps(different, indent=2)
